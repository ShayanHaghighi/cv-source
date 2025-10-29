local json = require("scripts/dkjson")
local file = io.open("skills.json", "r")
local content = file:read("*all")
file:close()

--
local data = json.decode(content)
local frameworks = data["frameworks"]
--
for i, f in ipairs(frameworks) do
    tex.print(f)
    if i ~= #frameworks then
        -- NO double backslashes needed here!
        -- Since the Lua code is *not* inside a LaTeX environment,
        -- you use the standard Lua escape for a single backslash: '\hfill'
        tex.print("\\hfill")
    end
end