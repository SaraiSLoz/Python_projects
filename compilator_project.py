#Develop by: Sarai Santiago Lozano
import turtle
import re
import os
#turtle library
t = turtle.Turtle()
#Regex a ocupar
regex_ef = r"EFR"
regex_at = r"ATR"
regex_gd = r"GD"
regex_gi = r"GI"
regex_sp = r"SP"
regex_bp = r"BP"
regex_cp = r"CP"
regex_lp = r"LP"
regex_cr = r"CR"
regex_rep = r"REP"
regex_par1 = r"\["
regex_par2 = r"\]"
regex_n = r"[1-9][0-9]*"
regex_num = r"[1-9][0-9]*(\.\d+)|[1-9][0-9]*|0"
regex_color = r"(white|black|red|green|blue|yellow|brown|gray|orange|pink)"

instrucciones = 1
ciclo = 0
#Functions that determine the error in the instructions of the user
def errorLog(tipo):
  global instrucciones
  print("Error en la linea: ", instrucciones)
  print(tipo)

def rerror(tipo, x):
  global instrucciones
  print("Error en la linea: ", instrucciones)
  print("Error en la instruccion: ", x, " del ciclo: ", ciclo)
  print(tipo)
#function repeat with recursion
def repeat(cmd,n,x, r):
  if(n==0):return
  if(x>=len(cmd)): 
    repeat(cmd, n-1, 0, 1)
    return
  if re.fullmatch(regex_ef,cmd[x]): # use fullmatch to check the string is accepting for the regex 
    try:
      if re.fullmatch(regex_num,cmd[x+1]):
        turtle.forward(int(cmd[x+1]))
        r += 1
        x += 2
        repeat(cmd, n, x, r)
        return
      else:
        s = cmd[x]
        s += " Solo recibe valores numericos"
        rerror(s,r)
        return
    except:
      s = cmd[x]
      s += " Falta parametro"
      r += 1
      rerror(s,r)
      return
    
  if re.fullmatch(regex_at,cmd[x]):  # Back instruction comparation 
    try:
      if re.fullmatch(regex_num, cmd[x+1]):
        turtle.backward(int(cmd[x+1]))
        r+=1
        x += 2
        repeat(cmd, n, x, r) #The function is recursively called n times as requested
        return
      else:
        s = cmd[x]
        s += " Solo recibe valores numericos"
        rerror(s,r)
        return
    except:
      s = cmd[x]
      s += " Falta parametro"
      r += 1
      rerror(s,r)
      return  
  if re.fullmatch(regex_gd, cmd[x]):  # Right instruction comparation
    try:
      if re.fullmatch(regex_num, cmd[x+1]):
        turtle.right(int(cmd[x+1]))
        r += 1
        x += 2
        repeat(cmd, n, x, r)
        return
      else:
        s = cmd[x]
        s += " Solo recibe valores numericos"
        rerror(s,r)
        return
    except:
      s = cmd[x]
      s += " Falta parametro"
      r += 1
      rerror(s,r)
      return  
  if re.fullmatch(regex_gi, cmd[x]):  # Left instruction comparation
    try:
      if re.fullmatch(regex_num, cmd[x+1]):
        turtle.left(int(cmd[x+1]))
        r+=1
        x += 2
        repeat(cmd, n, x, r)
        return
      else:
        s = cmd[x]
        s += " Solo recibe valores numericos"
        rerror(s,r)
        return
    except:
      s = cmd[x]
      s += " Falta parametro"
      r += 1
      rerror(s,r)
      return 
  if re.fullmatch(regex_sp, cmd[x]):  # pen down instruction comparation
      turtle.penup()
      r+=1
      x += 1
      repeat(cmd, n, x, r)
      return
    
  if re.fullmatch(regex_bp, cmd[x]):  # pen up instruction comparation
      turtle.pendown()
      r+=1
      x += 1
      repeat(cmd, n, x, r)
      return
    
  if re.fullmatch(regex_lp, cmd[x]):  # Pen clean instruction comparation 
      turtle.clean()
      r+=1
      x += 1
      repeat(cmd, n, x, r)
      return
    
  if re.fullmatch(regex_cr, cmd[x]):  # home instruction comparation 
      turtle.home()
      r += 1
      x += 1
      repeat(cmd, n, x, r)
      return
    
  if re.fullmatch(regex_cp, cmd[x]):  # Change color instruction comparation
    try:
      if re.fullmatch(regex_color, cmd[x+1]):
        turtle.color(cmd[x+1])
        r+=1
        x += 2
        repeat(cmd, n, x, r)  
        return 
      else:
        s = cmd[x]
        s += " Solo recibe parametros de tipo color"
        rerror(s,r)
        return
    except:
      s = cmd[x]
      s += " Falta parametro"
      r += 1
      rerror(s,r)
      return    

  s = cmd[x]
  s+= " Comando no existe"
  r += 1
  rerror(s,r)
  return
  
print('Escribe el archivo de las instrucciones:')
archivo = input()
if os.path.exists(archivo):
    print("---Leyendo archivo---\n")
    with open(archivo) as f: # Read the file .txt
      lines = f.read().splitlines()
else:
    print('No se encuentra archivo')

def syntax(lines, x): #Main function syntax for analyzing the instructions.
  global instrucciones
  global ciclo
  if(x>=len(lines)): return
  cmd = lines[x].split(" ")
  if re.fullmatch(regex_ef,cmd[0]): #forward instructions
    if re.fullmatch(regex_num,cmd[1]):
      turtle.forward(int(cmd[1]))
      instrucciones += 1
      x += 1
      syntax(lines, x)
      return
    else:
      instrucciones += 1
      s = cmd[0]
      s += " Solo recibe valores numericos" # Detected errors 
      errorLog(s)
      return
    
  if re.fullmatch(regex_at,cmd[0]):  #back instructions
    if re.fullmatch(regex_num, cmd[1]):
      turtle.backward(int(cmd[1]))
      instrucciones += 1
      x += 1
      syntax(lines, x)
      return
    else:
      instrucciones += 1
      s = cmd[0]
      s += " Solo recibe valores numericos" #check that the input is a numeric number
      errorLog(s)
      return
      
  if re.fullmatch(regex_gd, cmd[0]):  # lexeme for turn right instruction
    if re.fullmatch(regex_num, cmd[1]):
      turtle.right(int(cmd[1]))
      instrucciones += 1
      x += 1
      syntax(lines, x)
      return
    else:
      instrucciones += 1
      s = cmd[0]
      s += " Solo recibe valores numericos"
      errorLog(s)
      return
       
  if re.fullmatch(regex_gi, cmd[0]):  # lexeme for turn left instruction
    if re.fullmatch(regex_num, cmd[1]):
      turtle.left(int(cmd[1]))
      instrucciones+=1
      x += 1
      syntax(lines, x)
      return
    else:
      instrucciones += 1
      s = cmd[0]
      s += " Solo recibe valores numericos"
      errorLog(s)
      return
    
  if re.fullmatch(regex_sp, cmd[0]):  #  lexeme for pen up instruction
    turtle.penup()
    instrucciones+=1
    x += 1
    syntax(lines, x)
    return
    
  if re.fullmatch(regex_bp, cmd[0]):  # lexeme for pen down instruction
    turtle.pendown()
    instrucciones+=1
    x += 1
    syntax(lines, x)
    return
    
  if re.fullmatch(regex_lp, cmd[0]):  # lexeme for clean instruction
    turtle.clean()
    instrucciones+=1
    x += 1
    syntax(lines, x) #it call again the function
    return
    
  if re.fullmatch(regex_cr, cmd[0]):  # se detecta el lexema para levantar pluma
    turtle.home()
    instrucciones+=1
    x += 1
    syntax(lines, x)
    return
    
  if re.fullmatch(regex_cp, cmd[0]):  # se detecta el lexema para cambiar color
    if re.fullmatch(regex_color, cmd[1]):
      turtle.color(cmd[1])
      instrucciones += 1
      x += 1
      syntax(lines, x)  
      return
    else:
      s = cmd[x]
      s += " Solo recibe valores de tipo color"
      errorLog(s)
      return
  if re.fullmatch(regex_rep, cmd[0]): # detect the repeat function
    if re.fullmatch(regex_n, cmd[1]):  # detect a number before []
      n = (int(cmd[1]))
      if re.fullmatch(regex_par1, cmd[2]):  # detect "[]""
        if re.fullmatch(regex_par2, cmd[len(cmd)-1]):
          rcmd = cmd[3:len(cmd)-1]
          ciclo += 1
          repeat(rcmd,n,0,0) #Call function repeat
          x += 1
          syntax(lines, x)  
          return
        else: #Detect error
          instrucciones+=1
          s = "Falta cerrar "
          s+=cmd[2]
          errorLog(s)
          return
      else:
        instrucciones+=1
        s = "[ faltante despues de "
        s += cmd[1]
        errorLog(s)
        return
    else:
      instrucciones+=1
      s = cmd[0]
      s += " Recibe valores numericos"
      errorLog(s)
      return
  
  
  instrucciones+=1
  e = cmd[0]
  e += " Comando No Existe"
  errorLog(e)
  return

syntax(lines, 0)
