#!/usr/bin/env python3
"""Tenglish caption script: one entry per Whisper token in src/words_master.json (index order). '|' splits a token into two
words (second word time given or interpolated); '' drops the token (merged into the previous word)."""
TE = ["Guys,", "GTA", "6", "release", "ayyindi.", "Entha", "famous|ayyindo@3.60", "andariki", "telise", "untundi.",
      "Chaala", "mandiki", "GTA", "6", "ippati", "varaku", "13", "years", "enduku", "teeskundo", "teliyadu.",
      "Enduku?", "Adi", "story", "kosam", "kaadu,", "maps", "kosam", "kaadu,", "graphics", "kosam", "aithe", "assalu", "kaadu.",
      "Mari", "deniki", "", "anante?", "Adi", "money", "kosam,", "timing", "kosam.", "Normal ga,",
      "game", "release", "avuthundante", "konni", "samvatsaralu", "paatu", "baagane", "sale|avuthundi.", "Aa", "tarvatha", "daani", "hype|anedi",
      "gradual", "ga", "decrease", "avuthundi.", "Appudu", "developers", "malli", "next", "game", "meedha", "work", "chestharu.",
      "Kaani", "GTA", "5", "vishayamlo", "ala", "jaragaledu.", "Eppudaithe", "kotha", "game", "paatha", "game", "kante", "ekkuva", "profit",
      "teeskosthundo,", "appude", "daani", "release|cheyadaniki@40.85|alochistharu.@41.35",
      "So", "finally", "GTA", "6", "ni", "develop", "cheyadaniki", "13", "years", "pattaledu.", "GTA", "5", "kante", "GTA", "6", "ekkuva",
      "profit", "ayye", "varaku", "13", "years", "wait", "chesaru", "annamaata.",
      "Anthakanna", "important", "enti ante,", "so", "mana", "channel", "subscribe", "chesukondi."]
