import pygtk
import sys
import gtk
import os
global command, sort, path

class UserInterface:
	def destroy(self, widget, data = None):
		gtk.main_quit()
	
	def browse_print_path(self, widget) :
					
		dialog = gtk.FileChooserDialog("Open..",
					       None,
					       gtk.FILE_CHOOSER_ACTION_OPEN,
					       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
						gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)

		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)
		
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.gif")
		filter.add_pattern("*.tif")
		filter.add_pattern("*.xpm")
		dialog.add_filter(filter)

		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			self.textbox.set_text(dialog.get_filename())
		elif response == gtk.RESPONSE_CANCEL:
		    	self.textbox.set_text('No file selected')
		dialog.destroy()
	
	def on_changed(self, widget):
		global sort
		sort =  widget.get_active_text()
		if sort == "merge_sort":
			sort = "quick_sort"
		elif sort == "bubble_sort" or "selection_sort":
			sort = "insertion_sort"
			
	#	print sort
	
	def store(self, widget):
		self.obj =  self.textbox.get_text()
	#	print obj

	def get_text_box(self, widget):
		global path, command
		path = self.textbox.get_text()
	
		command = "java " + "main_class" + " " + path + " "+ sort
	#	print command
		os.system(command)
	#	print path
	#	print sort	
	#	gtk.main_quit()

	def get_file(self, widget, data = None) :
		
	#	os.system("/home/jayant/")
		dialog = gtk.FileChooserDialog("open..",
					       None,
					       gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
					       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
						gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)


		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			print "hi"			
		elif response == gtk.RESPONSE_CANCEL:
			self.textbox.set_text('No file selected')
		dialog.destroy()

	
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.window.set_size_request(400, 250)
		
		self.hbox = gtk.HBox()
		
		self.textbox = gtk.Entry()
		self.textbox.set_text('insert path of file to sort')
		self.textbox.select_region(0, len(self.textbox.get_text()))
		self.textbox.connect("changed", self.store)
	
		self.path_button = gtk.Button("browse_file")
		self.path_button.connect("clicked", self.browse_print_path)	
	
		self.hbox.pack_start(self.textbox)
		self.hbox.pack_start(self.path_button)
		
		self.button1 = gtk.Button("EXIT")
		self.button1.connect("clicked", self.destroy)
		
		self.button2 = gtk.Button("OK")
		self.button2.connect("clicked", self.get_text_box)

		self.button_file = gtk.Button("get_sorted_file")
		self.button_file.connect("clicked", self.get_file)
	
		self.cb = gtk.combo_box_new_text()
        	self.cb.connect("changed", self.on_changed)	

		self.cb.append_text('insertion_sort')
		self.cb.append_text('quick_sort')
        	self.cb.append_text('selection_sort')
        	self.cb.append_text('merge_sort')
		self.cb.append_text('bubble_sort')
		
  
		
		self.box1 = gtk.VBox()
		self.box1.pack_start(self.cb)
		self.box1.pack_start(self.hbox)
		self.box1.pack_start(self.button1) 
		self.box1.pack_start(self.button_file)
		self.box1.pack_start(self.button2) 
		self.window.add(self.box1)
		self.window.show_all()
		self.window.connect("destroy", self.destroy)
	
	def main(self) :
	#	global command 
		gtk.main()
	#	command = "java " + "main_class" + " " + path + " "+ sort
	#	print command
	#	os.system(command)
		return 0

if __name__ == "__main__": 
	base = UserInterface()
	base.main()	
	
