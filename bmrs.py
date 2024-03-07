# bmrs
def bmrs(word, i=1):
  if not word.startswith('_'):
    word = '_' + word
  if -1 < i < len(word):
    return interpret(word, i) + bmrs(word, i+1)
  return ''

# predecessor
def p(word, i):
	if i <= 1:
		return 0
	else:
		return i-1

# successor
def s(word, i):
	if i >= len(word) - 1:
		return 0
	else:
		return i+1

# interpreter function
def interpret(word, i):
  if H_o(word, i):
    return 'H'
  else:
    if L_o(word, i):
      return 'L'
    else:
      return '0'

# input predicate for high tones
def H_i(word, i):
  return word[i] == 'H'

# input predicate for low tones
def L_i(word, i):
  return word[i] == 'L'

# input predicate for out of bounds symbol
def out_of_bounds_i(word, i):
  return word[i] == "_"

def L_o(word,i):
  if L_i(word,i):
    return True
  else:
    return False

def H_o(word, i):
  if L_i(word,i):
    return False
  else:
    return c_i(word,i)


def c_i(word,i):
  if H_i(word,i):
    if a_i(word,i):
      return True
    else:
      return b_i(word,i)
  else:
    return d_i(word,i)

def a_i(word,i):
  if L_i(word,s(word,i)):
    return True
  else:
    return False

def b_i(word,i):
  if out_of_bounds_i(word, s(word,s(word,i))):
    if not out_of_bounds_i(word,i):
      return True
  else:
    return False

def d_i(word,i): #function_1 or function_2 or function_3
  if function_1(word,i):
    return True
  else:
    return function_23(word,i)

def function_23(word,i):
  if function_2(word,i):
    return True
  else:
    return function_3(word,i)

def function_1(word,i):
  if H_i(word,s(word,i)):
    if out_of_bounds_i(word, s(word,s(word,i))):
      return True
  else:
    return False

def function_2(word,i):
  if L_i(word,s(word,i)):
    if find_H_left(word, i):
      return True
  else:
    return False

def function_3(word,i):
  if b_i(word,i):
    if find_H_left(word, i):
      return True
  else:
    return False

def find_H_left(word, i):
  if word[i] == '_':
    return False
  if word[i] == 'L':
    return False
  if H_i(word, p(word, i)):
    return True
  else:
    return find_H_left(word, p(word, i))
