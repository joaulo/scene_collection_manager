![Blender Render Manager](https://www.joaulo.com/media/projects/project_scene-collection-manager/preview_big.jpg)
# scene_collection_manager

This addon derives from the need to work on a complex project with a PC with limited resources. To overcome the saturation of the hardware avoiding continuous slowdowns and crashes during the rendering phase, I made this addon to facilitate the selection of the active/excluded collections with a few clicks. It is currently in its first release and probably will grow over time with new features.


# Installation

It installs like a standard Blender addon, just download the .zip file on your PC, then go to *Blender> Edit> Preferences...*, use the *Install…* button and use the File Browser to select the .zip add-on file. For more information, refer to the [Blender manual page](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html?highlight=preferences).


# How does it work?

Once installed and activated, the addon interface will be visible in a dedicated panel called "*Scene Collections Manager*" in the "*Scene Properties*" section:

![Render Manager Panel](https://www.joaulo.com/media/uploads/2020/04/27/screenshot_20200427_131135_WzRKDyv.jpeg)

In order from top to bottom:

* **Load collection settings** (text field): select the *Collections* settings folder/file to load
* **Load Collection Settings** (button): start loading the settings from the selected file
* **Save collection settings** (text field): select the *Collections* settings folder/file to save
* **Save Collection Settings** (button): start saving the settings into the selected file

Currently *Collections* settings saved/loaded are related to their "**exclusion**" status, as shown in the outliner by the *checkbox* next to the name of the collection:

![Outliner](https://www.joaulo.com/media/uploads/2020/04/27/screenshot_20200427_143056.jpeg)

With this addon you can **activate or exclude** the *Collections* in the scene and save their status, then recall the same settings at a later time. This procedure is particularly useful if there is a need to work on a complex scene with a PC with limited resources.

Example: if in your scene there are several frames (cameras) to be rendered and in each camera/frame you can see only a portion of the scene, it is possible to "turn off" the unseen collections to reduce the system load during rendering or even just editing the selected view. By saving this setup for each view it is therefore possible to easily switch from one configuration to another with a few clicks.


# Limitations and known problems

* currently the extension of the files saved and loaded by the addon is not imposed, however it will be adopted the extension "*.scm*" in the future
* do not use the relative path in the selection of files or folders within the addon, use only absolute paths! Due to a still unresolved problem, using the relative path with the file or folder will result in an error message when executing the command. To use absolute paths, after clicking on the folder icon next to the selection field, use the following settings in the path selection window:

   * *select the gear icon at the top right:*

   ![path settings](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211442.jpeg)

   * *disable the checkbox:*

   ![checkbox_wrong](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211522.jpeg)
   ![checkbox_right](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211731.jpeg)

   * *verify that the path in the field is the full path to the file:*

   ![full_path](https://www.joaulo.com/media/uploads/2020/04/27/screenshot_20200427_131432.jpeg)


# TO DO

* manage file extension automatically
* add more selection settings to the manager: selection, show in 3D view and render (as shown in the Outliner by the icons:arrow, eye and monitor)
* add the status of the individual objects contained in the Collections to the configuration files
