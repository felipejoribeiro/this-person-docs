# Personal WIKI

Here resides all information concerning software development acquired through the ages. This include knowledge about web development, linux, information security and other related topics. The material is composed by notes that are scattered through directories and subdirectories organized by topic.

![library](./assets/books.png)

All files are in **MarkDown** format which is a lightweight markup language that allows plain text formating. The reason for it was that these plain text files are easily searchable with fuzzy finders and grep commands, which makes information queries really easy by grep commands.

An example for this was made when configuring **rofi** to search for these notes. This was made with a simple `bash` command:

```bash
ls -R ~/notes | grep -v README | grep .md | sed "s/;/ /g" | rofi -dmenu -p "Open"
```

Which open the chosen note in **Neovim** for editing or reading. And it's possible to convert these notes to `PDF` as well if required with **Pandoc**:

![gif](./assets/rofi.gif)

The dot files are located in this [Repo](https://github.com/felipejoribeiro/my-dev-environment).

## Authorship

All words here were written by myself and were based in a multitude of fonts that range from `Youtube` videos to `books` and academic `articles`. But, as these notes are intended for personal usage, rarely these fonts are mentioned in the text, only when strictly necessary for future research.

## Contributing

If you wish to contribute fell free to send a pull request. New information, revisions or corrections are highly welcome and appreciated.

## Licenses

[MIT](https://github.com/felipejoribeiro/this-person-docs/blob/main/LICENSE)
