text = "X-DSPAM-Confidence:    0.8475"
num_pos = text.find( '0' )
num = float(text[num_pos:])
print (num)
