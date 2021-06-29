VERSION = "0.3.0"

local micro = import("micro")
local config = import("micro/config")
local shell = import("micro/shell")
local buffer = import("micro/buffer")
local os = import("os")
local ospath = import("os.path")
local filepath = import("path/filepath")
local py = require 'python'
local content_completion = py.import "lsp/translate".content_completion


function AutoCompletePython(Buff)
    contents = "'''Test file for test_completion.'''
    
    
    def my_function():
        '''Simple test function.'''
        return 1
    
    
    my
    "
    line = 8
    col = 2
    results = content_completion("/home/phillip/.config/micro/plug/autocomp-lsp/lsp/test_data.py", contents, line, col)
    return results, results
end

function init()
    config.AddRuntimeFile("autocomp", config.RTHelp, "help/autocomp-lsp.md")
    buffer.TryBindAutocomplete("autocomp-lsp", "python", "AutoCompletePython")
end
