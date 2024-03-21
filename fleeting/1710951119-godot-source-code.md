---
id: 1710951119-godot-source-code
aliases:
  - godot-source-code
tags: []
---

# godot-source-code

## File system: directories and files

### The core directory

The most important directory in the **Godot** engine is `core`, everything else uses these modules. Everything in this directory is written in `C++` and is very low level.

In this directory the first thing to notice is the `typedefs.h` file. This is the most included file in the whole source code. It contains all the basic types and macros used in the engine.

It has:

- **config directory**: contains the loader of configuration files;
- **crypto directory**: contains the cryptographic functions;
- **debugger directory**: contains the debugger;
- **error directory**: contains the error handling macros;
- **extension directory**: has to do with the GDextension, handle **Godot** extensions;
- **input directory**: contains input low level functions;
- **io directory**: files, networking, serialization, formatting, input, output;
- **math directory;**
- **object directory**: contains the objects class, nodes;
- **os directory**: operating system abstractions;
- **string directory**: Unicode system for parsing strings, string manipulation;
- **templates directory;**
- **variant directory**: expose the basic types of the engine to the high level language. Inspector, communication through the internet, data type bindings;

And many files.

## The Servers directory

:
