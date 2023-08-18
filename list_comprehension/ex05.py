# Create a list of all the consonants in the string “Yellow Yaks like yelling
# and yawning and yesturday they yodled while eating yuky yams”

phrase = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
result = [consonant for consonant in phrase if consonant not in "aeiou "]

print(result)
