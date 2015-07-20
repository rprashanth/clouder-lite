# clouder-lite
A simple Python3-Flask application to turn a machine into a cloud storage system over Wi-Fi.

Use this app to start a server on your laptop and upload files from a phone or another laptop over Wi-Fi.

Get speeds greater than that of Bluetooth.

Absence of an OS in the list does not mean that it doesn't work on that OS but simply means that it hasn't been tested there. Please add any items, that are missing, to the list if you have verified it.

## Contents
* [Supported OS - Computer]()
* [Supported OS - Phone]()
* [Setup]()
* [Usage]()

### Supported OS - Computer

* Working
1. Ubuntu 14.04

* Not working

### Supported OS - Phone

* Working
1. Windows 8.1 Denim
 * Working
  * Internet Explorer
 * Not working
  * UC Browser - Multiple file selection unavailable; File system access unavailable;

* Not working

### Setup

For those of you are familiar with the Python environment:
* Create a virtual environment (Py3) and install all the dependencies mentioned in requirements.txt.
* Activate the venv and run `python3 server.py`.
* You can now access the said server from a phone by knowing the machine's inet address
 * `ifconfig` will help you find the inet address

### Usage

* Once you're connected to the server you will be presented with a form.
* Click browse and select all the files that you would like to upload.
* Click on `Upload` and wait for some time.
* Upload time will depend on the size of the file.
* You will be taken back to the form as soon as all the have been uploaded.
* Uploaded files will be present in the directory `clouder-lite/uploads/`. So make a note of where you are placing the folder `clouder-lite`
