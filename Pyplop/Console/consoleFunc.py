def log( data, console ):
    msg = " ".join(data.split(" ")[1:len(data)])
    
    try:
        print(exec(msg))
    except:
        print(f"{msg} its not global")

    newVr = console.font.render( msg, True, (255, 255, 255) )
    console.variables.append( newVr )
    

consoleFunc = {
    "log": log
}