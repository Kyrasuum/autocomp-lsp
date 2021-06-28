VERSION = "3.5.0"

local micro = import("micro")
local config = import("micro/config")
local shell = import("micro/shell")
local buffer = import("micro/buffer")
local os = import("os")
local ospath = import("os.path")
local filepath = import("path/filepath")

function AutoCompleteC(Buff){
    return "test1\ntest2\ntest3", "test1\ntest2\ntest3"
}

function init()
    config.AddRuntimeFile("autocomp", config.RTHelp, "help/autocomp-lsp.md")
    buffer.TryBindAutocomplete("autocomp-lsp", "C", "AutoCompleteC")
    buffer.TryBindAutocomplete("autocomp-lsp", "c", "AutoCompleteC")
    buffer.TryBindAutocomplete("autocomp-lsp", "c++", "AutoCompleteC")
    buffer.TryBindAutocomplete("autocomp-lsp", "lua", "AutoCompleteC")
end
