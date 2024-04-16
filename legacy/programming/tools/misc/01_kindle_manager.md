# Managing kindle from the terminal.
With the tools mentioned here you will be capable of:

- Send `non-Kindle` books to `kindle`.
- Read `Kindle` books on `Linux`.

You might have a library of books locally in your machine, and you can send then to you kindle for a better read experience. If you have a `PDF` book you can read it on kindle but it's advised to convert it to the `MOBI` extension for a better experience in the defice. Some `PDF`s can't be converted but most can.

## Converging from PDF to MOBI
To convert from `PDF` to `MOBI` you can use the `Calibre` package. It's open source. It is available in `pacman`. There you can import the books and then convert then clicking in then with the right mouse button.

The `Willus` package is a wanderfull application to optimizes PDF to be much more readable in the kindle. Awesome for articles, for example. Here it is: https://www.willus.com/k2pdfopt/

## Adding books to your kindle
You can transfer the files via usb, which is the simlest way. By connecting and mounting the kindle as an external storage device, the books will show up and then you can deleto or add books at will.

Files are very disorganized there, it's not very funny to explore. 

The other way of doing this is by email. You have to configure it in your amazon account by going on Settings -> All Settings -> My account -> Send-to-Kindle Email. Then, you can send the MOBI file to the address and the document will pop up in your kindle the next time you connect to the internet.

The supported file types are:

- Microsoft Word (.DOC, .DOCX)
- HTML (.HTML, .HTM)
- RTF (.RTF)
- JPEG (.JPEG, .JPG)
- Kindle Format (.MOBI, .AZW)
- GIF (.GIF)
- PNG (.PNG)
- BMP (.BMP)
- PDF (.PDF)

For pdf files you can send "convert" in the subject of the email to convert it to `.azw` that is a file format that enables good functionalities like anotations, whispersync and font size.

Other option, based on the email method is with the `sendKindle` utility. With this tool you can send the documents directly to your kindle via terminal. It is a python library. Here you can see its github page: https://github.com/kparal/sendKindle

You can install the utility with `pip3 install --user sendKindle`. Then just configure it and send the documents with the `sendKindle` command, or if you need to convert you can make the `sendKindle -c` command. When you run the program for the first time it will create the following config file in `/home/<user_name>/.config/sendKindle/sendKindle.cfg`, with the following text:

```cfg
[Default]
smtp_server = smtp.gmail.com
smtp_port = 465
smtp_login = username
user_email = username@gmail.com
kindle_email = username@free.kindle.com
# optional
smtp_password = password
convert = False
```
So, you must enter your kindle credentials and email credentials. (but that doesn't seems very secure, as you will need to configure your gmail account to allow non secure logins, and your password will be available in plain text in your system). Maybe it's better to create a "test" email just to disable security features to this functionality to work. But i don't recommend using it with your main gmail account.

## Finding books
Here are some ways of finding books to download in a legal manner:

- https://www.gutenberg.org/ : 54000 free classical books.

- https://werebooks.org/ : More classical books for free.

- https://standardebooks.org/ : The library from gutenberg but in a more readable version.

- https://www.humblebundle.com/?partner=itsfoss : Not free, but good freaking deals and and part of the sale goes to charity.

- https://www.baen.com/allbooks/category/index/id/2012 : Free library of science fiction and fantasy books. You can purchase stuff too.






