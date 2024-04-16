# Initialization process in Neovim
Here we will study the initialization process of the `nvim` editor.
When the editor is initialized the following things happens:
- The `$SHELL` option is setted from the environment.
- Process the arguments like options and file name. Buffers are created for all files (but not loaded). `-V` can be used to display logs from these actions.
- If `--embed` is used, it waits for a `UI` to connect before loading user configurations.
- Load user config. (execute commands from files, environment,...). It executes the files (init init.vim init.lua vimrc exrc). Using vim and lua at the same time isn't recommended. If you use `-u` the steps before are skipped and the configuration file isn't loaded. Locations searched for initializations, in order of preference:
	- $VIMINIT environment variable (Ex command line).
	- User |config|: $XDG_CONFIG_HOME/nvim/init.vim.
	- Other config: {dir}/nvim/init.vim where {dir} is any directory
	   in $XDG_CONFIG_DIRS.
	- $EXINIT environment variable (Ex command line).
	|$MYVIMRC| is set to the first valid location unless it was already
	set or when using $VIMINIT.
- If the 'exrc' option is on (which is NOT the default), the current
	directory is searched for two files.  The first that exists is used,
	the others are ignored.
	-  The file ".nvimrc"
	-  The file ".exrc"
- Enable filetype and indent plugins if `-u` isn't used.
- Enable syntax highlighting. Same as run `syntax`.
- Load the plugin scripts. Same as `:runtime! plugin/**/*.vim`. Loading plugins won't be done when:
	- The 'loadplugins' option was reset in a vimrc file.
	- The |--noplugin| command line argument is used.
	- The |--clean| command line argument is used.
	- The "-u NONE" command line argument is used |-u|.
	- When Vim was compiled without the |+eval| feature.
- Set 'shellpipe' and 'shellredir' from your `$SHELL` value.
- Set the `updatecount` to zero, if `-n` command argument is used.
- Set binary options.
- Read the shaDa file.
- Read the quickfix file.
- Open all windows.	When the |-o| flag was given, windows will be opened (but not displayed yet). When the |-p| flag was given, tab pages will be created (but not displayed yet). When switching screens, it happens now.  Redrawing starts. If the "-q" flag was given to Vim, the first error is jumped to. Buffers for all windows will be loaded, without triggering |BufAdd| autocommands.
- Execute startup commands
	- If a "-t" flag was given to Vim, the tag is jumped to.
	- The commands given with the |-c| and |+cmd| arguments are executed.
	- If the 'insertmode' option is set, Insert mode is entered.
	- The starting flag is reset, has("vim_starting") will now return zero.
	- The |v:vim_did_enter| variable is set to 1.
	- The |VimEnter| autocommands are executed.








