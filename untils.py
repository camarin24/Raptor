import os, sys, time

def get_size(the_path):
    """Get size of a directory tree or a file in bytes."""
    path_size = 0.0
    for path, directories, files in os.walk(the_path):
        for filename in files:
            path_size += os.lstat(os.path.join(path, filename)).st_size
        for directory in directories:
            path_size += os.lstat(os.path.join(path, directory)).st_size
    path_size += os.path.getsize(the_path)
    return path_size

def main():
    argv = sys.argv[1]
    if argv == "help":
        print "\nstats\nfreespace\n"
    if argv == 'stats':
        print "\n##### Raptor stats ######\n"
        print "Tiempo del servidor          : " + time.strftime("%H:%M:%S") + "|" + (time.strftime("%d/%m/%y"))
        print "Total titulos descargados    : " + str(len(os.listdir("/home/davidpaisa/Web/appmusic/"))) + "\tarchivos"
        print "Total titulos indexados      : " + str(len(os.listdir("/home/davidpaisa/Web/data/")) - 1) + "\tarchivos"
        print "Espacio en disco 'appmusic'  : " + str(round(float(((get_size("/home/davidpaisa/Web/appmusic/")/1024)/1024)/1024), 2)) + "\tGigaBytes Aprox."
        print "Espacio en disco 'data'      : " + str(round(float((get_size("/home/davidpaisa/Web/data/")/1024)/1024), 2)) + "\tMegaBytes Aprox."
        print ""
    if argv == 'freespace':
        if len(sys.argv) <= 2:
            print "\nUSE: freespace <folder> <percentage to drop>\n"
            return
        folder = sys.argv[2]
        #Saber si el directorio existe
        if not os.path.exists(folder):
            print "\nERROR: Directory not found '"+folder+"'\n"
            return;
        percentage = sys.argv[3]
        #Saber si el porcentage es correcto
        if percentage.isdigit():
            if int(percentage) > 100:
                print "\nERROR: Percentage '"+percentage+"' cannot exceed 100\n"
                return
            if int(percentage) <= 0:
                print "\nERROR: Percentage '"+percentage+"' cannot be less than 0\n"
                return
        else:
            print "\nERROR: it's not a number '"+percentage+"'\n"
            return
        listFiles = os.listdir(folder)
        totalToDrop = int((float(percentage)/100)*len(listFiles))
        print "'\nSe borrara un total de '"+str(totalToDrop)+"' archivos al azar."
        dialog = raw_input("[y/n] para continuar...\n")
        if dialog.lower() in "y":
            for i in xrange(0,totalToDrop):
                #print folder+listFiles[i]
                os.remove(folder+listFiles[i])
            print "Se eliminaron '"+str(totalToDrop)+"' archivos al azar.\n"
        else:
            print "No se elimino ningun archivo :)\n"
        
if __name__ == '__main__':
    main()
