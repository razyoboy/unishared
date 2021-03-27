# ----- Imports ----------------------
import wx
import os
import glob
import time
import random
import eyed3
import wx.media
import wx.lib.buttons as buttons

# ----- File Directory -------------------------------
directory = os.path.dirname(os.path.abspath(__file__))
imgdirectory = os.path.join(directory, "Picture")
sd_song_path = os.path.join(directory, "song")
playlist_name = ""
playlist_path = os.path.join(directory, "Playlist")

# ----- Main Panel -----------------------------------
class MusicPanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.title = "Title"
        self.artist = "Artist"
        self.album = "Album"
        self.current_time = "00:00"
        self.volume = 15

        self.songname = ""
        self.song_path = ""
        self.curSong = 0
        self.row_obj_dict = {}  # Dictionary of all item in song list
        self.song = {}  # Dictionary for mp3 file of the song

        self.create_menu()  # create the menu bar
        self.layout_constructor()  # create all the widget

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.song_timer)
        self.timer.Start(100)

    def layout_constructor(self):  # Create all widget

        # ----- Media Control -----
        try:
            self.mediaPlayer = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER)
        except NotImplementedError:  # raised when the program didn't override the method of the base class
            self.Destroy()

        self.mediaPlayer.Bind(wx.media.EVT_MEDIA_FINISHED, self.when_loop)

        # Sizer -----
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        left_sizer = wx.BoxSizer(wx.VERTICAL)  # Left side ( library tree, playlist tree )
        right_sizer = wx.BoxSizer(wx.VERTICAL)  # Right side ( media control panel and song list )
        top_right_sizer = wx.BoxSizer(wx.VERTICAL)  # Media panel
        sub_top_right = wx.BoxSizer(wx.HORIZONTAL)  # Inside Media panel
        lower_right_sizer = wx.BoxSizer(wx.VERTICAL)  # Song list

        # Library -----

        self.build_library_tree(left_sizer)
        self.build_playlists(left_sizer)

        subfolders = [f.name for f in os.scandir(playlist_path) if f.is_dir()]  # Name of all playlist folder
        for name in subfolders:
            self.add_to_playlist(name)

        # ----- Media Control & Song list -----

        # ----- Media Control -----

        # Now Playing Box -----
        np_box = wx.StaticBox(self, size=(720,90))
        np_box_sizer = wx.StaticBoxSizer(np_box, wx.VERTICAL)
        firstline_sizer = wx.BoxSizer(wx.HORIZONTAL)
        secondline_sizer = wx.BoxSizer(wx.HORIZONTAL)
        timeslider_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.np_title = wx.StaticText(self, style=wx.ALIGN_CENTER)
        self.np_title.SetLabel(self.title)
        firstline_sizer.Add(self.np_title, 0, wx.ALIGN_CENTER)

        self.np_artist = wx.StaticText(self, style=wx.ALIGN_CENTER)
        self.np_artist.SetLabel(self.artist)

        self.np_album = wx.StaticText(self, style=wx.ALIGN_CENTER)
        self.np_album.SetLabel(self.album)

        firstline_sizer.Add(self.np_artist, 0, wx.ALIGN_CENTER)
        firstline_sizer.Add(self.np_album, 0, wx.ALIGN_CENTER)

        self.currTime = wx.StaticText(self, style=wx.ALIGN_CENTER)
        self.currTime.SetLabel(self.current_time)

        secondline_sizer.Add(self.currTime, 0, wx.ALIGN_CENTER)

        np_box_sizer.Add(firstline_sizer, 0, wx.ALIGN_CENTER)
        np_box_sizer.Add(secondline_sizer, 0, wx.ALIGN_CENTER)

        self.song_slider = wx.Slider(self, size=wx.DefaultSize)
        self.song_slider.Bind(wx.EVT_SLIDER, self.time_offset)

        timeslider_sizer.Add(self.song_slider, 1, wx.ALL | wx.EXPAND, 5)

        np_box_sizer.Add(timeslider_sizer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND)

        top_right_sizer.Add(np_box_sizer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND)

        top_right_sizer.Add((-1,10))  # Adding blank space
        # ---------------------

        # buttons

        self.build_media_control(sub_top_right)

        top_right_sizer.Add(sub_top_right, flag=wx.LEFT, border=10)
        top_right_sizer.Add((-1,10))  # Adding blank space

        # Song List -----

        self.build_songlist(lower_right_sizer)

        # -----

        # Main sizer for right side

        right_sizer.Add(top_right_sizer, 0)
        right_sizer.Add(lower_right_sizer, -1, wx.EXPAND | wx.ALL)

        # -----

        # Main sizer for the panel

        main_sizer.Add(left_sizer, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        main_sizer.Add(right_sizer, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        self.SetSizer(main_sizer)

    def create_menu(self):  # Create menu bar
        """
        Menu bar containing Import new folder, Create new playlist and Quit
        """
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()

        open_folder_menu = file_menu.Append(wx.ID_ANY, "&Import", "Open a file")
        create_playlist = file_menu.Append(wx.ID_ANY, "&Create Playlist", "Create a new playlist")
        quit_program = file_menu.Append(wx.ID_ANY, "&Quit", "Quit the program")

        menu_bar.Append(file_menu, "&File")

        self.parent.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_folder,
            source=open_folder_menu,
        )

        self.parent.Bind(
            event=wx.EVT_MENU,
            handler=self.create_playlist,
            source=create_playlist
        )

        self.parent.Bind(
            event=wx.EVT_MENU,
            handler=self.on_quit,
            source=quit_program
        )

        self.parent.SetMenuBar(menu_bar)

    def create_playlist(self, event):  # Create new playlist
        dialog = wx.DirDialog(self, "Create a playlist folder", style=wx.DD_DEFAULT_STYLE)

        if dialog.ShowModal() == wx.ID_OK:
            name = os.path.basename(dialog.GetPath())
            self.add_to_playlist(name)

        dialog.Destroy()

    def add_to_playlist(self, name):  # Add newly created playlist to treectrl
        self.playlisttree.AppendItem(self.playlist_root, name)

    def update_playlist_view(self, event):  # Update the songlist to song in playlist
        name = self.playlisttree.GetItemText(event.GetItem())
        path = os.path.join(playlist_path, name)
        self.update_songlist(path)

    def build_playlists(self, sizer):  # Create treectrl of playlist

        self.playlisttree = wx.TreeCtrl(self, size=(200, 100))
        self.playlist_root = self.playlisttree.AddRoot("Playlists")
        self.playlisttree.Expand(self.playlist_root)

        sizer.Add(self.playlisttree, wx.EXPAND, border=10)

        self.playlisttree.Bind(wx.EVT_TREE_SEL_CHANGED, self.update_playlist_view)

    def build_library_tree(self, sizer):  # Create treectrl for library

        librarytree = wx.TreeCtrl(self, size=(200, 100))
        library_root = librarytree.AddRoot("Library")

        librarytree.AppendItem(library_root, "Song")
        librarytree.Expand(library_root)

        sizer.Add(librarytree, border=10)

        librarytree.Bind(wx.EVT_TREE_SEL_CHANGED, self.library_pressed)

    def build_songlist(self, sizer):  # Create list to display a song

        self.songlist = wx.ListCtrl(self, style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SORT_ASCENDING)
        self.songlist.InsertColumn(0, "Title", width=210)
        self.songlist.InsertColumn(1, "Artist", width=175)
        self.songlist.InsertColumn(2, "Album", width=170)
        self.songlist.InsertColumn(3, "Genre", width=160)

        sizer.Add(self.songlist, -1, wx.ALL | wx.EXPAND)
        self.songlist.Bind(wx.EVT_LIST_ITEM_SELECTED, self.loadMusic)

        self.update_songlist(sd_song_path)

    def update_songlist(self, folder):  # Update songlist when new songs are added
        self.song_path = folder
        self.songlist.ClearAll()

        self.songlist.InsertColumn(0, "Title", width=210)
        self.songlist.InsertColumn(1, "Artist", width=175)
        self.songlist.InsertColumn(2, "Album", width=170)
        self.songlist.InsertColumn(3, "Genre", width=160)

        songs = glob.glob(folder + "/*.mp3")
        song_objects = []
        index = 0
        for song in songs:
            song_object = eyed3.load(song)
            self.songlist.InsertItem(index, song_object.tag.title)
            self.songlist.SetItem(index, 1, song_object.tag.artist)
            self.songlist.SetItem(index, 2, song_object.tag.album)
            self.songlist.SetItem(index, 3, song_object.tag.genre.name)
            song_objects.append(song_object)
            self.song[index] = song
            self.row_obj_dict[index] = song_objects
            index += 1

    # Build media control panel including buttons and slider
    def build_media_control(self, sizer):
        """
        buttondata is the dictionary for button containing image of the button, handler and name
        """

        # ------ Buttons ------
        button_data = [{"image": "previous.png", "handler": self.previous_song, "name": "prev_btn"},
                       {"image": "stop.png", "handler": self.on_stop, "name": "stop_btn"},
                       {"image": "next.png", "handler": self.next_song, "name": "next_btn"}]

        shuffle_data = {"image": "shuffle.png", "handler": self.when_shuffle, "name": "shuffle_btn"}
        img = wx.Bitmap(os.path.join(imgdirectory, "shuffle.png"))
        self.shuffle_btn = buttons.GenBitmapButton(self, bitmap=img, name="shuffle", size=(40,40))

        self.shuffle_btn.Bind(wx.EVT_BUTTON, handler=self.when_shuffle)
        sizer.Add(self.shuffle_btn, wx.LEFT)

        self.build_button(button_data[0], sizer)

        img = wx.Bitmap(os.path.join(imgdirectory, "play.png"))
        self.playpause_btn = buttons.GenBitmapToggleButton(self, bitmap=img, name="play", size=(40, 40))

        img = wx.Bitmap(os.path.join(imgdirectory, "pause.png"))
        self.playpause_btn.SetBitmapSelected(img)

        self.playpause_btn.Bind(wx.EVT_BUTTON, handler=self.on_play)
        sizer.Add(self.playpause_btn, wx.LEFT)

        self.build_button(button_data[1], sizer)
        self.build_button(button_data[2], sizer)

        img = wx.Bitmap(os.path.join(imgdirectory, "loop.png"))
        self.loop_btn = buttons.GenBitmapToggleButton(self, bitmap=img, name="loop", size=(40, 40))

        img = wx.Bitmap(os.path.join(imgdirectory, "on_loop.png"))
        self.loop_btn.SetBitmapSelected(img)

        self.loop_btn.Bind(wx.EVT_BUTTON, handler=self.is_loop_down)
        sizer.Add(self.loop_btn, wx.LEFT)

        # ------ Volume Slider ------

        # Image of volume slider
        low_vol = wx.Bitmap(os.path.join(imgdirectory, "low_vol.png"))
        high_vol = wx.Bitmap(os.path.join(imgdirectory, "high_vol.png"))

        static_low = wx.StaticBitmap(self)
        static_low.SetBitmap(low_vol)

        static_high = wx.StaticBitmap(self)
        static_high.SetBitmap(high_vol)

        sizer.Add((100, 0))
        sizer.Add(static_low, wx.LEFT)

        # Volume slider
        self.vol_slider = wx.Slider(self)
        self.vol_slider.SetRange(0,100)
        self.vol_slider.SetValue(self.volume)
        self.vol_slider.Bind(wx.EVT_SLIDER, self.vol_control)

        sizer.Add(self.vol_slider, wx.LEFT)
        sizer.Add((30,0))

        sizer.Add(static_high, wx.LEFT)

    def build_button(self, button_dict, sizer):  # Build bitmap button
        """
        build the button and bind the event to button built
        """

        img = button_dict["image"]
        handler = button_dict["handler"]
        name = button_dict["name"]

        button_img = wx.Bitmap(os.path.join(imgdirectory, img))
        button = buttons.GenBitmapButton(self, bitmap=button_img, name=name, size=(40,40))
        button.Bind(wx.EVT_BUTTON, handler)

        sizer.Add(button, wx.LEFT)

    # handler when play button is pressed
    def on_play(self, event):
        """
        GetIsDown() true if the toggle button is pressed

        Second condition check if the media is playable or not
        if not raise the error message box
        """

        if not event.GetIsDown():
            self.on_pause()
            return

        if not self.mediaPlayer.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?",
                          "ERROR",
                          wx.ICON_ERROR | wx.OK)
        else:
            self.mediaPlayer.SetInitialSize()
            self.GetSizer().Layout()
            self.song_slider.SetRange(0, self.mediaPlayer.Length())

        event.Skip()

    # handler for pause button
    def on_pause(self):
        """
        Pause the media
        """
        self.mediaPlayer.Pause()

    # handler for next song button
    def next_song(self, event):
        """
        index is the position of row of song in the song list
        when the button is pressed
        it will check if the index is more than the last song or not
        if not it will load next song
        but if it is it will load the first song of the list
        """
        index = self.curSong + 1
        self.playpause_btn.SetToggle(True)
        if index < len(self.song):
            self.loadSong(index)
        elif index > (len(self.song)-1):
            self.loadSong(0)
        self.timer.Start(100)

    # handler for previous song button
    def previous_song(self, event):
        """
        when the button is pressed
        it will check if the index less than the first song or not
        if it is the program will load the last song of the list
        """
        index = self.curSong - 1
        self.playpause_btn.SetToggle(True)
        if index >= 0:
            self.loadSong(index)
        elif index < 0:
            self.loadSong(len(self.song) - 1)

    # handler when shuffle button is pressed
    def when_shuffle(self, event):
        """
        Random the index of the song list
        so that when the button is pressed
        it will random the song
        """
        index = random.randint(0, len(self.song) - 1)
        self.loadSong(index)
        self.mediaPlayer.Play()
        self.playpause_btn.SetToggle(True)

    # handler when stop button is pressed
    def on_stop(self, event):
        """
         Stop the media player and set the toggle button to off
        """
        self.mediaPlayer.Stop()
        self.playpause_btn.SetToggle(False)

    # handler when the media finished playing
    def when_loop(self, event):
        """
        Check if the button is pressed
        if it is rewind the time slider to 0 and start playing the media again
        """
        if self.loop_btn.GetValue():
            self.mediaPlayer.Seek(0)
            self.mediaPlayer.Play()
        event.Skip()

    # handler of loop button
    def is_loop_down(self, event):
        """
        This function is just a signal
        for when_loop button to be called if the button is pressed
        """
        return

    # handler of volume slider
    def vol_control(self, event):
        """
        Receive value from volume slider
        then set the value of the media player
        """
        self.volume = self.vol_slider.GetValue()
        self.mediaPlayer.SetVolume(self.volume)

    # handler for time slider
    def time_offset(self, event):
        """
        Get the offset from the slider
        then set the time of the media
        """
        offset = self.song_slider.GetValue()
        self.mediaPlayer.Seek(offset)

    # handler to count time of the media
    def song_timer(self, event):
        """
        Get the offset by the time of the media
        then the program will update the time slider
        and also update the time label
        """
        offset = self.mediaPlayer.Tell()
        self.song_slider.SetValue(offset)
        self.current_time = time.strftime("%M:%S", time.gmtime(offset//1000))
        self.currTime.SetLabel(self.current_time)

    # handler of treectrl
    def library_pressed(self, event):
        """
        update the song list to list of the playlist
        """
        self.update_songlist(sd_song_path)

    # Load song by index
    def loadSong(self, index=0):
        """
        Get the index of the songlist
        tags is dictionary of song list containing every song in the songlist
        The program will extract the metadata from mp3 file the add to the list
        """
        self.curSong = index
        tags = self.row_obj_dict[index]

        self.title = tags[index].tag.title
        self.np_title.SetLabel(self.title)
        self.artist = tags[index].tag.artist
        self.np_artist.SetLabel(self.artist)
        self.album = tags[index].tag.album
        self.np_album.SetLabel(self.album)

        if index >= 0:
            mp3 = self.song[index]
            if not self.mediaPlayer.Load(mp3):
                wx.MessageBox("Unable to load media", wx.ICON_ERROR | wx.OK)
            else:
                self.mediaPlayer.Play()
                self.playpause_btn.SetToggle(True)
                self.mediaPlayer.SetInitialSize()
                self.GetSizer().Layout()
                self.song_slider.SetRange(0, self.mediaPlayer.Length())

    # Load song by event from list
    def loadMusic(self, event):
        """
        selection is the index of song from songlist
        self.curSong will get the index from selection for other function to use
        """
        self.selection = self.songlist.GetFocusedItem()
        self.curSong = self.selection
        self.playpause_btn.SetToggle(False)
        tags = self.row_obj_dict[self.selection]

        self.title = tags[self.selection].tag.title
        self.np_title.SetLabel(self.title)
        self.artist = tags[self.selection].tag.artist
        self.np_artist.SetLabel(self.artist)
        self.album = tags[self.selection].tag.album
        self.np_album.SetLabel(self.album)

        if self.selection >= 0:
            mp3 = self.song[self.selection]
            if not self.mediaPlayer.Load(mp3):
                wx.MessageBox("Unable to load media", wx.ICON_ERROR | wx.OK)
            else:
                self.on_pause()
                self.mediaPlayer.SetInitialSize()
                self.GetSizer().Layout()
                self.song_slider.SetRange(0, self.mediaPlayer.Length())

    # Dialog for importing the song library
    def on_open_folder(self, event):

        dialog = wx.DirDialog(self, "Choose a folder", style=wx.DD_DEFAULT_STYLE)

        if dialog.ShowModal() == wx.ID_OK:
            self.update_songlist(dialog.GetPath())

        dialog.Destroy()

    # Quit the program
    def on_quit(self, event):
        self.parent.Close()

# ----- Main Window -------------------------------
class MusicAppFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None, title = "Untitled Music App", size = (1000, 720))
        self.panel = MusicPanel(self)
        self.Show()

def main():
    app = wx.App(False)
    frame = MusicAppFrame()
    app.MainLoop()

if __name__ == "__main__":
    main()