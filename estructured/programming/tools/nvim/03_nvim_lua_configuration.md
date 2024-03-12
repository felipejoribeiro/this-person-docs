# Configuring Nvim with Lua
Integrating lua with vim is awesome as it enables more customization. And the legend says that it becomes faster. So let's start trying to understand how vim deals with the language. You can place your lua files inside `/nvim/lua/` folder. Lets start with the file `tools.lua`:

```lua
-- in tools.lua
local api = vim.api
local M = {}
function M.makeScratch()
	api.nvim_command('enew') --equivalent to :enew
	vim.bo[0].buftype=nofile -- set the current buffer's (buffer 0) bufType to no file
	vim.bo[0].bufhidden=hide
	vim.bo[0].swapfile=false

end
return M
```

We will use M to avoid things in our global scope.


