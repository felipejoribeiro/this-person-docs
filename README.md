# Personal WIKI

Here resides all information concerning software development acquired through the ages. This include knowledge about web development, linux, information security and other related topics. The material is composed by notes that are scattered through directories and subdirectories organized by topic.

![library](./data/books.png)

All files are in **MarkDown** format which is a lightweight markup language that allows plain text formating. The reason for it was that these plain text files are easily searchable with fuzzy finders and grep commands, which makes information queries really easy by grep commands.

An example for this was made when configuring **rofi** to search for these notes. This was made with a simple `bash` command:

```bash
ls -R ~/notes | grep -v README | grep .md | sed "s/;/ /g" | rofi -dmenu -p "Open"
```

Which open the chosen note in **Neovim** for editing or reading. And it's possible to convert these notes to `PDF` as well if required with **Pandoc**:

![gif](./data/rofi.gif)

The dot files are located in this [Repo](https://github.com/felipejoribeiro/my-dev-environment).

## Authorship

All words here were written by myself and were based in a multitude of fonts that range from `Youtube` videos to `books` and academic `articles`. But, as these notes are intended for personal usage, rarely these fonts are mentioned in the text, only when strictly necessary for future research.

## Contributing

If you wish to contribute fell free to send a pull request. New information, revisions or corrections are highly welcome and appreciated.

## Zettelkasten

"Slip box" in German, the method was created by Niklas Luhmann, a German sociologist. It's a method of note taking based on little documents linked to one another. You have the _zettel_ which is a note and the _kasten_ which is the container. Here we implement this method with markdown files as the notes and directories as the containers.

About the notes, there are three categories:

- **Permanent notes**: are created by revising and synthesizing fleeting notes and literature notes. They are intended to be permanent and are the main source of knowledge.
- **Literature notes**: notes that are taken from content that is not created by the author. It has references to the original content, and synthesis of the content.
- **Fleeting notes**: momentary notes that are not intended to be permanent. Authoral ideas, thoughts and reflections.

Niklas says that the productivity of a knowledge worker is directly related to the amount of permanent notes that he produces per day.

Each note must represent a single idea. As they represent building blocks of knowledge.

Interesting enough, this isn't a top down knowledge method, which divides knowledge in categories, but it's the opposite, it starts from the ideas and then it leaves to the links between notes to create the organization. It's the greatest multidisciplinary method of knowledge building.

## Licenses

[MIT](https://github.com/felipejoribeiro/this-person-docs/blob/main/LICENSE)
