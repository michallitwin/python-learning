import time, datetime, threading

#A)

    #startTime = datetime.datetime(2026, 5, 16, 16, 4, 0)

    #while datetime.datetime.now() < startTime:
    #   time.sleep(1)
    #print('Program now starting on maj 16 -16:04')

#B)
    #print('Start of program.')
    #def takeANap():
    #    time.sleep(5)
    #    print('Wake up!')
    #target tutaj wskazuje ze takanap ma byc odpalone w tle, gdy nadejdzie czas odpal ta funkcje 
    #threadObj = threading.Thread(target=takeANap)
    #start() tworzy niezalezny watek programu i go odpala 
    #threadObj.start()

    #print('End of program.')


#C)
threadObj = threading.Thread(target=print, args=['abc', 'michal', 'adsadas123'], kwargs={'sep': ' @!@# '})
t2 = threading.Thread(target=print, args=['aamba', 'qwerty', 'rewq'], kwargs={'sep': ' ** '})
t2.start()
threadObj.start()

