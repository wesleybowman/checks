while True:
    a=subprocess.check_output(["qstat"])
    m=re.search(r'\br\b',a)
    if m!=None:
        print 'Done'
        break
