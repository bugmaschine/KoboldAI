gensettingstf = [
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Output Length",
	"id": "setoutput", 
	"min": 16,
	"max": 512,
	"step": 2,
	"default": 80,
    "tooltip": "Number of tokens to be generated. Higher values will take longer to generate.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "genamt",
    "ui_level": 0
	},
   {
	"uitype": "slider",
	"unit": "float",
	"label": "Temperature",
	"id": "settemp", 
	"min": 0.1,
	"max": 2.0,
	"step": 0.01,
	"default": 0.5,
    "tooltip": "Randomness of sampling. Higher values can increase creativity, but make the output less meaningful. Lower values will make the output more predictable, but it may become more repetitive.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "temp",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top P Sampling",
	"id": "settopp", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 0.9,
    "tooltip": "Used to discard unlikely text in the sampling process. Lower values will make the output more predictable, but also repetitive. (Put this value on 1 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_p",
    "ui_level": 1
    
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Top K Sampling",
	"id": "settopk",
	"min": 0,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "Alternative sampling method. Can be combined with top_p. (Put this value on 0 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_k",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Tail Free Sampling",
	"id": "settfs", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 1.0,
    "tooltip": "Alternative sampling method. It is recommended to disable top_p and top_k (set top_p to 1 and top_k to 0) if this setting is used. 0.95 is a suggested value for this setting. (Put this value on 1 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "tfs",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Typical Sampling",
	"id": "settypical", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 1.0,
    "tooltip": "Alternative sampling method. Described in the paper \"Typical Decoding for Natural Language Generation\" (10.48550/ARXIV.2202.00666). The paper indicates 0.2 as a suggested value for this setting. (Put this value on 1 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "typical",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top A Sampling",
	"id": "settopa", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 0.0,
    "tooltip": "Alternative sampling method. Reduces the randomness of the AI whenever the probability of one token is much higher than all the others. Higher values have a stronger effect. (Put this value on 0 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_a",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Repetition Penalty",
	"id": "setreppen", 
	"min": 1.0,
	"max": 3.0,
	"step": 0.01,
	"default": 1.1,
    "tooltip": "Used to penalize words that were already generated or belong to the context.",
    "menu_path": "Settings",
    "sub_path":  "Repetition",
    "classname": "model",
    "name": "rep_pen",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Rep Pen Range",
	"id": "setreppenrange", 
	"min": 0,
	"max": 4096,
	"step": 4,
	"default": 0,
    "tooltip": "Repetition penalty range. If set higher than 0, only applies repetition penalty to the last few tokens of the story rather than applying it to the entire story. The slider controls the amount of tokens at the end of your story to apply it to.",
    "menu_path": "Settings",
    "sub_path":  "Repetition",
    "classname": "model",
    "name": "rep_pen_range",
    "ui_level": 1
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Rep Pen Slope",
	"id": "setreppenslope", 
	"min": 0.0,
	"max": 10.0,
	"step": 0.1,
	"default": 0.0,
    "tooltip": "Repetition penalty slope. If both this setting and Rep Penalty Range are set higher than 0, will use sigmoid interpolation to apply repetition penalty more strongly on tokens that are closer to the end of the story. Higher values will result in the repetition penalty difference between the start and end of your story being more apparent. (Setting this to 1 uses linear interpolation; setting this to 0 disables interpolation)",
    "menu_path": "Settings",
    "sub_path":  "Repetition",
    "classname": "model",
    "name": "rep_pen_slope",
    "ui_level": 1
	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Alt Rep Pen",
 	"id": "use_alt_rep_pen",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Applies repetition penalty as a logarithmic modifier rather than a linear modifier.",
    "menu_path": "Settings",
    "sub_path": "Repetition",
    "classname": "model",
    "name": "use_alt_rep_pen",
    "ui_level": 2
 	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Context Tokens",
	"id": "settknmax", 
	"min": 512,
	"max": 2048,
	"step": 8,
	"default": 1024,
    "tooltip": "Number of context tokens to submit to the AI for sampling. Make sure this is higher than Output Length. Higher values increase VRAM/RAM usage.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "max_length",
    "ui_level": 0
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Gens Per Action",
	"id": "setnumseq", 
	"min": 1,
	"max": 5,
	"step": 1,
	"default": 1,
    "tooltip": "Number of generated output choices. Increases VRAM/RAM usage.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "numseqs",
    "ui_level": 0
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "WI Depth",
	"id": "setwidepth", 
	"min": 1,
	"max": 5,
	"step": 1,
	"default": 3,
    "tooltip": "Number of actions from the end of the story to scan for World Info keys.",
    "menu_path": "World Info",
    "sub_path": "",
    "classname": "user",
    "name": "widepth",
    "extra_classes": "var_sync_alt_system_alt_gen",
    "ui_level": 2
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Auto Save",
	"id": "autosave", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Whether the story is saved after each action.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "story",
    "name": "autosave",
    "ui_level": 0
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Contextual Prompt",
	"id": "setuseprompt", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 1,
    "tooltip": "Whether the prompt should be sent in the context of every action.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "story",
    "name": "useprompt",
    "ui_level": 2
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Adventure Mode",
	"id": "setadventure", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Turn this on if you are playing a Choose your Adventure model.",
    #"menu_path": "Story",
    #"sub_path": "",
    #"classname": "story",
    #"name": "adventure"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Chat Mode",
	"id": "setchatmode", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "This mode optimizes KoboldAI for chatting.",
    #"menu_path": "Story",
    #"sub_path": "",
    #"classname": "story",
    #"name": "chatmode"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Dynamic WI Scan",
	"id": "setdynamicscan", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Scans the AI's output for World Info keys as it is generating the one.",
    "menu_path": "World Info",
    "sub_path": "",
    "classname": "story",
    "name": "dynamicscan",
    "ui_level": 1
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "No Prompt Gen",
	"id": "setnopromptgen", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "If enabled, the AI does not generate a continuation of the entered prompt. Instead, you must perform an action first.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "user",
    "name": "nopromptgen",
    "ui_level": 2
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Prefilled Memory",
	"id": "setrngpersist",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "If enabled, the Memory box in Random Story will be filled with the memory of the current story instead of being empty.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "user",
    "name": "rngpersist",
    "ui_level": 2
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "No Genmod",
	"id": "setnogenmod",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Disables the userscripts' ability to edit output.",
    "menu_path": "Settings",
    "sub_path": "Modifiers",
    "classname": "user",
    "name": "nogenmod",
    "ui_level": 2
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Debug",
	"id": "debug",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Shows debug information.",
    "menu_path": "",
    "sub_path": "",
    "classname": "user",
    "name": "debug"
	},
    {
    "uitype": "dropdown",
	"unit": "text",
	"label": "Game Mode",
	"id": "storymode",
	"default": 0,
    "tooltip": "Select KoboldAI mode.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "story",
    "name": "storymode",
    'children': [{'text': 'Story', 'value': 0}, {'text':'Adventure','value':1}, {'text':'Chat', 'value':2}],
    "ui_level": 0
    },
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Streaming",
 	"id": "setoutputstreaming",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Shows tokens as they are generated.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "output_streaming",
    "ui_level": 1
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Probabilities",
 	"id": "setshowprobs",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Adds context menu to the output showing what other words were considered as it was generated.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "show_probs"
    ,
    "ui_level": 2
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Alt Text Gen",
 	"id": "alttextgen",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Inserts World Info entries behind text that first triggers them for better context with unlimited depth.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "alt_gen",
    "ui_level": 2
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Alt Multi Gen",
 	"id": "alt_multi_gen",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Runs Gens per Action one at a time so you can select one if you like it without having to wait.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "model",
    "name": "alt_multi_gen",
    "ui_level": 2,
    "extra_classes": "var_sync_alt_system_experimental_features"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Trim Sentences",
 	"id": "frmttriminc",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Deletes the text after the last sentence closure. If no closure is found, all tokens are returned.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmttriminc",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Blank Lines",
 	"id": "frmtrmblln",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Replaces double newlines (\\n\\n) with single ones to avoid blank lines.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmblln",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Special Chars",
 	"id": "frmtrmspch",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Removes special characters (@,#,%,^, etc).",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmspch",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Auto Spacing",
 	"id": "frmtadsnsp",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Adds spaces automatically if necessary.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtadsnsp",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Single Line",
 	"id": "singleline",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Allows the AI to generate an output only before the enter.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "singleline",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Double Spaces",
 	"id": "remove_double_space",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Removes any double spaces in the output.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "remove_double_space",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "slider",
 	"unit": "int",
 	"label": "AN Depth",
 	"id": "singleline",
 	"min": 1,
 	"max": 5,
 	"step": 1,
 	"default": 3,
	"tooltip": "Number of actions from the end of the story to insert Author's Note info.",
    "menu_path": "author_notes",
    "sub_path": "",
    "classname": "story",
    "name": "andepth",
    "ui_level": 2
 	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Show Field Budget",
	"id": "setshowbudget",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Shows the number of tokens when typing in text boxes. May cause lags."
	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Beep on Complete",
 	"id": "beep_on_complete",
 	"min": 1,
 	"max": 5,
 	"step": 1,
 	"default": 3,
	"tooltip": "If enabled, you will hear a beeping sound when generation or model loading is complete.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "beep_on_complete",
    "ui_level": 0
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "dropdown",
	"unit": "text",
	"label": "Image Priority",
	"id": "img_gen_priority",
	"default": 1,
    "tooltip": "Determines where the image will be generated.",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_priority",
    'children': [{'text': 'Use Local Only', 'value': 0}, {'text':'Prefer Local','value':1}, {'text':'Prefer Horde', 'value':2}, {'text':'Use Horde Only', 'value':3}, {'text':'Use Local SD-WebUI API', 'value':4}],
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "text",
	"unit": "text",
	"label": "Img API URL",
	"id": "img_gen_api_url",
	"default": "",
    "tooltip": "The URL to use when selecting Use Local SD-WebUI API setting in Image Priority",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_api_url",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "text",
	"unit": "text",
	"label": "Art Guide",
	"id": "img_gen_art_guide",
	"default": "",
    "tooltip": "The art guide sent with image gen requests. <|> (optional) is replaced with the story summary, otherwise the art guide is appended to the summary. \nDefault: masterpiece, digital painting, <|>, dramatic lighting, highly detailed, trending",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_art_guide",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "text",
	"unit": "text",
	"label": "Negative Prompt",
	"id": "img_gen_negative_prompt",
	"default": "",
    "tooltip": "Enter features you do not want generated in your images here, only works for img_gen_api. \nDefault:  lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_negative_prompt",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "slider",
	"unit": "int",
	"label": "Steps",
	"id": "img_gen_steps",
    "min": 15,
	"max": 50,
	"step": 1,
	"default": "30",
    "tooltip": "Set the number of iterations the image generator will use to refine your image.\nDefault:30",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_steps",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "slider",
	"unit": "float",
	"label": "Cfg Scale",
	"id": "img_gen_cfg_scale",
    "min": 1,
	"max": 30,
	"step": 0.5,
	"default": "7",
    "tooltip": "Set how strictly the AI will follow prompts, 5-15 are good values.\nDefault:7",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_cfg_scale",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Model in Memory",
 	"id": "keep_img_gen_in_memory",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "If enabled, the system will keep the model in memory, speeding up image generation time.",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "system",
    "name": "keep_img_gen_in_memory",
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Experimental UI",
 	"id": "experimental_features",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "If enabled, experimental features will be displayed in the UI.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "system",
    "name": "experimental_features"
    ,
    "ui_level": 2
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Generate Audio",
 	"id": "gen_audio",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "If enabled, The system will generate audio files for each action.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "story",
    "name": "gen_audio",
    "extra_classes": "var_sync_alt_system_experimental_features"
    ,
    "ui_level": 1
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "text",
	"unit": "text",
	"label": "Privacy Password",
	"id": "privacy_password",
	"default": "",
    "tooltip": "The password to unblur the UI when Ctrl+L is hit.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "privacy_password",
    "ui_level": 1
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "dropdown",
	"unit": "text",
	"label": "Chat Style",
	"id": "chat_style",
	"default": 0,
    "tooltip": "How chat messages are shown",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "story",
    "name": "chat_style",
	"extra_classes": "var_sync_alt_system_experimental_features",
    "children": [
		{"text": "Legacy", "value": 0},
		{"text": "Messages", "value": 1},
	],
    "ui_level": 1
 	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Full Determinism",
	"id": "setfulldeterminism",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Causes generation to be fully deterministic. The model will always generate the same thing as long as your story, settings and RNG seed are the same. If disabled, only the sequence of outputs the model generates is deterministic.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "full_determinism",
    "ui_level": 2
	},
    {
    "UI_V2_Only": True,
	"uitype": "toggle",
	"unit": "bool",
	"label": "Use AI Seed",
	"id": "seed_specified",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "If enabled a specfic seed will be used for the random generator on text generation",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "seed_specified",
    "ui_level": 2
	},
    {
	"uitype": "text",
	"unit": "text",
	"label": "RNG seed",
	"id": "seed",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "The seed number used to generate the AI text. Output will change if this number is changed.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "seed",
    "extra_classes": "var_sync_alt_system_seed_specified",
    "ui_level": 2
	},
    {
    "UI_V2_Only": True,
	"uitype": "dropdown",
	"unit": "int",
	"label": "UI Mode",
	"id": "ui_level",
	"min": 0,
	"max": 2,
	"step": 1,
	"default": 0,
    "tooltip": "How complex you want the UI.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "user",
    "name": "ui_level",
    "ui_level": 0,
    "children": [
		{"text": "Simple", "value": 0},
		{"text": "Advanced", "value": 1},
        {"text": "Power User", "value": 2}
	],
	},
    {
    "UI_V2_Only": True,
	"uitype": "slider",
	"unit": "int",
	"label": "Randomness",
	"id": "simple_randomness",
	"min": -100,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "How random the AI should be. Negative numbers is less random, positive is more random.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "model",
    "name": "simple_randomness",
    "extra_classes": "simple_ui_only var_sync_alt_user_ui_level",
    "ui_level": 0
	},
    {
    "UI_V2_Only": True,
	"uitype": "slider",
	"unit": "int",
	"label": "Creativity",
	"id": "simple_creativity",
	"min": -100,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "How creative the AI should be. Negative numbers is less creative, positive is more creative.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "model",
    "name": "simple_creativity",
    "extra_classes": "simple_ui_only var_sync_alt_user_ui_level",
    "ui_level": 0
	},
    {
    "UI_V2_Only": True,
	"uitype": "slider",
	"unit": "int",
	"label": "Repetiveness",
	"id": "simple_repitition",
	"min": -100,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "How repetitive the AI should be. Negative numbers is less repetitive, positive is more repetitive.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "model",
    "name": "simple_repitition",
    "extra_classes": "simple_ui_only var_sync_alt_user_ui_level",
    "ui_level": 0
	},
    {
    "UI_V2_Only": True,
	"uitype": "slider",
	"unit": "int",
	"label": "WI Gen Amount",
	"id": "wigen_amount",
	"min": 25,
	"max": 125,
	"step": 1,
	"default": 80,
    "tooltip": "How many tokens the World Info Generator creates.",
    "menu_path": "World Info",
    "sub_path": "",
    "classname": "user",
    "name": "wigen_amount",
    "ui_level": 2
	},
    {
    "UI_V2_Only": True,
	"uitype": "toggle",
	"unit": "bool",
	"label": "Native WI Gen",
	"id": "wigen_use_own_wi", 
	"default": False,
    "tooltip": "Uses your existing applicable (has title, type, content) World Info entries as inspiration for generated ones.",
    "menu_path": "World Info",
    "sub_path": "",
    "classname": "user",
    "name": "wigen_use_own_wi",
    "ui_level": 2
	},
]

gensettingsik =[{
	"uitype": "slider",
	"unit": "float",
	"label": "Temperature",
	"id": "settemp", 
	"min": 0.1,
	"max": 2.0,
	"step": 0.05,
	"default": 0.5,
    "tooltip": "Randomness of sampling. Higher values can increase creativity, but make the output less meaningful. Lower values will make the output more predictable, but it may become more repetitive.",
    "menu_path": "Model",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "temp"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top P Sampling",
	"id": "settopp", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.05,
	"default": 1.1,
    "tooltip": "Used to discard unlikely text in the sampling process. Lower values will make the output more predictable, but also repetitive. (Put this value on 1 to disable its effect)",
    "menu_path": "Model",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_p"
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Top K Sampling",
	"id": "settopk",
	"min": 0,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "Alternative sampling method. Can be combined with top_p.",
    "menu_path": "Model",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_k"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Tail Free Sampling",
	"id": "settfs", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.05,
	"default": 0.0,
    "tooltip": "Alternative sampling method. It is recommended to disable (set to 0) top_p and top_k if this setting is used. 0.95 is a suggested value for this setting. (Put this value on 1 to disable its effect)",
    "menu_path": "Model",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "tfs"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Output Length",
	"id": "setikgen", 
	"min": 50,
	"max": 3000,
	"step": 2,
	"default": 200,
    "tooltip": "Number of tokens to be generated. Higher values will take longer to generate.",
    "menu_path": "Model",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "max_length"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "WI Depth",
	"id": "setwidepth", 
	"min": 1,
	"max": 5,
	"step": 1,
	"default": 3,
    "tooltip": "Number of actions from the end of the story to scan for World Info keys.",
    "menu_path": "User",
    "classname": "user",
    "name": "widepth"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Auto Save",
	"id": "autosave", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Whether the story is saved after each action.",
    "menu_path": "Story",
    "classname": "story",
    "name": "autosave"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Stored Prompt",
	"id": "setuseprompt", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 1,
    "tooltip": "Whether the prompt should be sent in the context of every action.",
    "menu_path": "Story",
    "classname": "story",
    "name": "useprompt"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Adventure Mode",
	"id": "setadventure", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Turn this on if you are playing a Choose your Adventure model.",
    #"menu_path": "Story",
    #"classname": "story",
    #"name": "adventure"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Chat Mode",
	"id": "setchatmode", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "This mode optimizes KoboldAI for chatting.",
    #"menu_path": "Story",
    #"classname": "story",
    #"name": "chatmode"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "No Prompt Gen",
	"id": "setnopromptgen", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "If enabled, the AI does not generate a continuation of the prompt. Instead, you must perform an action first.",
    "menu_path": "User",
    "classname": "user",
    "name": "nopromptgen"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Prefilled Memory",
	"id": "setrngpersist",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "If enabled, the Memory box in Random Story will be filled with the memory of the current story instead of being empty.",
    "menu_path": "User",
    "classname": "user",
    "name": "rngpersist"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Debug",
	"id": "debug",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Shows debug information.",
    "menu_path": "User",
    "classname": "user",
    "name": "debug"
	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Streaming",
 	"id": "setoutputstreaming",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Shows tokens as they are generated.",
    "menu_path": "User",
    "classname": "user",
    "name": "output_streaming"
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Probabilities",
 	"id": "setshowprobs",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Adds context menu to output showing what other words were considered as it was generated.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "show_probs"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Alt Text Gen",
 	"id": "alttextgen",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Inserts World Info entries behind text that first triggers them for better context with unlimited depth.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "alt_gen"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Trim Sentences",
 	"id": "frmttriminc",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Deletes the text after the last sentence closure. If no closure is found, all tokens are returned.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmttriminc"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Blank Lines",
 	"id": "frmtrmblln",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Replaces double newlines (\\n\\n) with single ones to avoid blank lines.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmblln"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Special Chars",
 	"id": "frmtrmspch",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Removes special characters (@,#,%,^, etc).",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmspch"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Auto Spacing",
 	"id": "frmtadsnsp",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Adds spaces automatically if necessary.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtadsnsp"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Single Line",
 	"id": "singleline",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Allows the AI to generate an output only before the enter.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "singleline"
 	},
]

formatcontrols = [{
    "label": "Trim incomplete sentences",
    "id": "frmttriminc",
    "tooltip": "Deletes the text after the last sentence closure. If no closure is found, all tokens are returned."
    },
    {
    "label": "Remove blank lines",
    "id": "frmtrmblln",
    "tooltip": "Replaces double newlines (\\n\\n) with single ones to avoid blank lines."
    },
    {
    "label": "Remove special characters",
    "id": "frmtrmspch",
    "tooltip": "Removes special characters (@,#,%,^, etc)."
    },
    {
    "label": "Automatic spacing",
    "id": "frmtadsnsp",
    "tooltip": "Adds spaces automatically if necessary."
    },
    {
    "label": "Single Line",
    "id": "singleline",
    "tooltip": "Allows the AI to generate an output only before the enter."
    }]
