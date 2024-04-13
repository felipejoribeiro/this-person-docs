---
id: 1711122353-nvim-plugins-creation
aliases:
  - nvim-plugins-creation
tags:
  - engineering
  - neovim
  - lua
---

# Neovim plugins: an introduction

<span style="text-align: center; width: 100%; font-size: 0.75em">

An article about how to create **Neovim** plugins with the `lua` programming language. With a step by step guide and explanations about nvim's API and integrations.

</span>

![magic-circle-header.png](../assets/from_notes/1711122353-nvim-plugins-creation-2024-03-22-13-36-56-magic-circle-header.png)

---

Writing plugins in neovim is a simple task. It uses the `lua` programming language. So, as a first plugin, you can create `helloWorld.nvim` which prints `Hello World`:

```lua
function HelloWorld()
  print("Hello World")
end
```

For testing this code you can just create a new lua buffer and input the code above, them you can source it with `:so %`, which makes nvim execute the code. To execute the code you can do the following command:
`:lua HelloWorld()`, which will execute the function that you created.

You can create an user command as well with this updated version:

```lua
function HelloWorld()
  print("Hello World")
end

vim.api.nvim_create_user_command("HelloWorld",HelloWorld, {})
vim.api.nvim_create_autocmd("CursorHold", {callback = HelloWorld })
vim.keymap.set("n", "<leader>h", HelloWorld)
```

In this case, to execute the code, after sourcing the file, you can just make the `:HelloWorld` command or only holding the cursor in a location will trigger it. You can use the keymap as well. So these are the different ways of triggering our code.

Now, with the basics of the API, we can check how to distribute our extension.

## ✅ - The structure of neovim plugins

The basic structure of a **neovim** plugin is the following one:

```
    MyNvimPluging
    |
    |   lua
    |   |   PluginName
    |   |   |
    |   |   |   init.lua
```

Here is an example of `init.lua` file:

```lua
-- lua/PLuginName/init.lua
local M = {}
M.HelloWorld = function() print("Hello world!") end
return M
```

Whatever is returned from this `init.lua` command will be available to the user. And by creating a **GitHub** repository with this structure, any one who reference your plugin in their package manager will have access to the functionality.

To local development, depending on the package manager, you can select a local directory where your plugin resides. In **Lazy** package manager, for example, the following configuration will work:

```lua
return {
  "felipejoribeiro/svgo.nvim",
  dir = "~/work/personal/svgo.nvim",
  dependencies = { "rcarriga/nvim-notify" },
  opts = {
    illustration_dir = "../assets/from_notes",
  },
}
```

So, with this configuration, **neovim** will source your plugin's code from the given path.

## ✅ - Plugin live update

A common problem in plugin development is that, after you make a modification in your plugin you can't see the results immediately because **Neovim** caches all plugin information on startup. But you can add to your plugin a command to reload it and activate this function in a dev environment:

```lua
vim.api.create_user_command("ReloadMyPlugin", function()
    package.loaded.PluginName = nil
    require("PluginName").setup({})
end, {})
```

But be careful not to send this to production as this command will clutter your user interface with the plugin.

## ✅ - Plugin configuration

Dealing with the configuration of your plugin is a common task. You can get user configurations by using the `setup` function. Which is a development pattern in **Neovim** plugins. The user will call this function to configure the plugin and pass it's options. Then, inside the plugin you can read these values, and integrate with the default:

```lua
local plugin_options
local default_options = {
    my_opt_1 = 'Oranges',
    my_opt_2 = 'Apples',
}

M = {}

M.setup = function(options)
    options = options or {}
    plugin_options = vim.tbl_extend('keep', options, default_options)
end
```

It's important to note that the `vim.tbl_extend` function will prioritize the user options over the default ones. So, if the user doesn't pass any options, the default ones will be used.

## ✅ - Example plugin

Here we have a single file plugin to use as a final example.

```lua
-- lua/print_treesitter_target/init.lua
local my_plugin_opts
local default_opts = {
    target = 'comment',
    filter_text = '----',
}

M = {}

M.setup = function(opts)
    opts = opts or {}
    my_plugin_opts = vim.tbl_extend('keep', opts, default_opts)
end

local query = '((' .. my_plugin_opts.target .. ') @'
    .. my_plugin_opts.target
    .. ' (#match? @' .. my_plugin_opts.target .. ' "'
    .. my_plugin_opts.filter_text .. '")) @capture'

local parser = require('nvim-treesitter.parsers').get_parser()
local query = vim.treesitter.parse_query(parser:lang(), query)
local tree = parser:parse()[1]

function M.print_treesitter_target()
    local captures = query:iter_captures(tree:root(), 0)
    for _, n in captures do
        local text = vim.treesitter.get_node_text(n, 0)
        print(text)
    end
end

vim.api.nvim_create_user_command(
    "PrintTreesitterTarget",
    M.print_treesitter_target,
    {}
)

return M
```

So, configuring your plugin manager to use this plugin will make it available to the user. which will be able to use the `:PrintTreesitterTarget` command to print the target of the treesitter.
