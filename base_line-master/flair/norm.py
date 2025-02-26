import pandas as pd
import re


def normalize(norm):
    norm = norm.replace("ሃ", "ሀ")
    norm = norm.replace("ሐ", "ሀ")
    norm = norm.replace("ሓ", "ሀ")
    norm = norm.replace("ኅ", "ሀ")
    norm = norm.replace("ኻ", "ሀ")
    norm = norm.replace("ኃ", "ሀ")
    norm = norm.replace("ዅ", "ሁ")
    norm = norm.replace("ሗ", "ኋ")
    norm = norm.replace("ኁ", "ሁ")
    norm = norm.replace("ኂ", "ሂ")
    norm = norm.replace("ኄ", "ሄ");
    norm = norm.replace("ዄ", "ሄ");
    norm = norm.replace("ኅ", "ህ");
    norm = norm.replace("ኆ", "ሆ");
    norm = norm.replace("ሑ", "ሁ");
    norm = norm.replace("ሒ", "ሂ");
    norm = norm.replace("ሔ", "ሄ");
    norm = norm.replace("ሕ", "ህ");
    norm = norm.replace("ሖ", "ሆ");
    norm = norm.replace("ኾ", "ሆ");
    norm = norm.replace("ሠ", "ሰ");
    norm = norm.replace("ሡ", "ሱ");
    norm = norm.replace("ሢ", "ሲ");
    norm = norm.replace("ሣ", "ሳ");
    norm = norm.replace("ሤ", "ሴ");
    norm = norm.replace("ሥ", "ስ");
    norm = norm.replace("ሦ", "ሶ");
    norm = norm.replace("ሼ", "ሸ");
    norm = norm.replace("ቼ", "ቸ");
    norm = norm.replace("ዬ", "የ");
    norm = norm.replace("ዲ", "ድ");
    norm = norm.replace("ጄ", "ጀ");
    norm = norm.replace("ፀ", "ጸ");
    norm = norm.replace("ፁ", "ጹ");
    norm = norm.replace("ፂ", "ጺ");
    norm = norm.replace("ፃ", "ጻ");
    norm = norm.replace("ፄ", "ጼ");
    norm = norm.replace("ፅ", "ጽ");
    norm = norm.replace("ፆ", "ጾ");
    norm = norm.replace("ዉ", "ው");
    norm = norm.replace("ዴ", "ደ");
    norm = norm.replace("ቺ", "ች");
    norm = norm.replace("ዪ", "ይ");
    norm = norm.replace("ጪ", "ጭ");
    norm = norm.replace("ዓ", "አ");
    norm = norm.replace("ዑ", "ኡ");
    norm = norm.replace("ዒ", "ኢ");
    norm = norm.replace("ዐ", "አ");
    norm = norm.replace("ኣ", "አ");
    norm = norm.replace("ዔ", "ኤ");
    norm = norm.replace("ዕ", "እ");
    norm = norm.replace("ዖ", "ኦ");
    norm = norm.replace("ኚ", "ኝ");
    norm = norm.replace("ሺ", "ሽ");

    norm = re.sub('(ሉ[ዋአ])', 'ሏ', norm)
    norm = re.sub('(ሙ[ዋአ])', 'ሟ', norm)
    norm = re.sub('(ቱ[ዋአ])', 'ቷ', norm)
    norm = re.sub('(ሩ[ዋአ])', 'ሯ', norm)
    norm = re.sub('(ሱ[ዋአ])', 'ሷ', norm)
    norm = re.sub('(ሹ[ዋአ])', 'ሿ', norm)
    norm = re.sub('(ቁ[ዋአ])', 'ቋ', norm)
    norm = re.sub('(ቡ[ዋአ])', 'ቧ', norm)
    norm = re.sub('(ቹ[ዋአ])', 'ቿ', norm)
    norm = re.sub('(ሁ[ዋአ])', 'ኋ', norm)
    norm = re.sub('(ኑ[ዋአ])', 'ኗ', norm)
    norm = re.sub('(ኙ[ዋአ])', 'ኟ', norm)
    norm = re.sub('(ኩ[ዋአ])', 'ኳ', norm)
    norm = re.sub('(ዙ[ዋአ])', 'ዟ', norm)
    norm = re.sub('(ጉ[ዋአ])', 'ጓ', norm)
    norm = re.sub('(ደ[ዋአ])', 'ዷ', norm)
    norm = re.sub('(ጡ[ዋአ])', 'ጧ', norm)
    norm = re.sub('(ጩ[ዋአ])', 'ጯ', norm)
    norm = re.sub('(ጹ[ዋአ])', 'ጿ', norm)
    norm = re.sub('(ፉ[ዋአ])', 'ፏ', norm)
    norm = re.sub('[ቊ]', 'ቁ', norm)
    norm = re.sub('[ኵ]', 'ኩ', norm)
    #norm = re.sub('\s+', ' ', norm)

    return norm


with open('sst_test.txt','r',encoding='utf8') as fin:
    with open('sst_test2.txt', 'w', encoding='utf8', newline="") as f:
         for line in fin:
             f.write(normalize(line))




