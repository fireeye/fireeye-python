### Version 1.2.4
- Added function to submit URLs to the DoD service
- Added function to get the health of the DoD service
### Version 1.1.0
- Reverted the file_submit function back to 0.1.0 since the body parameter is used for additional options and specifying file size cutoffs is not the preferred way to handle large files.
- Added the get_artifact() function.
### Version 1.0.0
- Changed parameters for submit_file function.  Eliminated the "body" parameter since it isn't needed, added "file_name" parameter to name the file, and added parameter "contents" to put the binary contents of the file.
- Added an option to the submit_file function to specify how many bytes from the beginning of a file to send to the detection service.  Default is the first 32 MB, but is configurable to any positive integer.   