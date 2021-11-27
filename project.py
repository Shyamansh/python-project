from flask import Flask,  jsonify 
import json
import requests
from bs4 import BeautifulSoup

print("**************************Welcome to the JUIT scraper API on local host server**************************")

print("""Enter '1' for getting important nortification from the JUIT website
Enter '2' for getting Android development internship's from intershala
Enter '3' for getting Game development internship's from intershala.
Enter '4' for getting IOS development internship's from intershala
Enter '5' for getting Data science internship's from intershala
Enter '6' for getting internship data from the intershala
Enter '7' for exiting the program.""")
case = int(input('Enter your choice: - '))

while case != 7:

    if(case == 1):
        app = Flask(__name__)
        @app.route('/')
        def Software_Development_internships():
            all_answers = []                                                   #list for getting the json files to post to local server as without it it dosent work
            html_text = requests.get('https://www.juit.ac.in/importantnotification').text                  #link for juit notification page

            soup= BeautifulSoup (html_text,'lxml')


            notification = soup.find_all('tr')
            link=soup.find_all('a')
        


            for x in notification:                                 #notification name use randomy for limiting forloop to required number of iteration(we can use anything if it limits the loop accordint to requirement)
                for NT,lnk in zip(notification,link):               #zip takes iterable or containers and returns a single iterator object, having mapped values from all the containers.
                
                    #name below are only here as these need formatting
                    NT = NT.text.replace('\n','').replace('\t','').replace('Link','').replace('#','')
                    #name above are only here as these need formatting


                    answer={
                        'Notification: ' : NT,
                        'Link' : lnk['href']
                        }

                    queries_json = json.dumps(answer)
                    all_answers.append(queries_json)

            return jsonify (all_answers)




        if __name__ == '__main__':
            app.run(debug=False, host='0.0.0.0', port=88)                         #JUIT information page


#case 2
    elif (case == 2):
        start_link='https://internshala.com'

        app = Flask(__name__)
        @app.route('/')
        def Android_Development_internships():
            '''Function provide data for Android development internship's from intershala.'''
            all_answers = []
            html_text = requests.get('https://internshala.com/internships/android-internship').text                  #for game development
            soup= BeautifulSoup (html_text,'lxml')


            company_name= soup.find_all('div', class_="heading_4_5 profile")
            stipend = soup.find_all(('span'), class_="stipend")
            location = soup.find_all(('a'), class_="location_link")
            start_date = soup.find_all(('div'), class_="item_body", id="start-date-first")
            link_to = soup.find_all(('div'),class_="heading_4_5 profile")



            for x in zip(company_name):
                for name, sal, loc, Sdate, LK in zip(company_name, stipend, location, start_date, link_to):                            #zip takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
    
                    #name below are only here as these need formatting
                    nm = name.text.replace('\n','')                                         #name of company
                    dt = Sdate.text.replace('\n','').replace('Immediately','').strip()      #date of joining as intern
                    #name above are only here as these need formatting

                    answer={
                        'Company name' : nm,
                        'Stipend' :  sal.text,
                        'Location': loc.text,
                        'Date of joining as intern' : dt,
                        'For more information link for internship': start_link+LK.a['href']
                        }

                    queries_json = json.dumps(answer)
                    all_answers.append(queries_json)

            return jsonify (all_answers)







        if __name__ == '__main__':
            app.run(debug=False, host='0.0.0.0', port=5000)



#case 3
    elif(case == 3):
        app = Flask(__name__)
        @app.route('/')
        def game_development_internship():
            '''Function provide data for game development internship's from intershala.'''
            all_answers = []
            html_text = requests.get('https://internshala.com/internships/game%20development-internship').text                  #for game development
            soup= BeautifulSoup (html_text,'lxml')


            company_name= soup.find_all('div', class_="heading_4_5 profile")
            stipend = soup.find_all(('span'), class_="stipend")
            location = soup.find_all(('a'), class_="location_link")
            start_date = soup.find_all(('div'), class_="item_body", id="start-date-first")
            link_to = soup.find_all(('div'),class_="heading_4_5 profile")


            for x in zip(company_name):
                for name, sal, loc, Sdate, LK in zip(company_name, stipend, location, start_date, link_to):                            #zip takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
   
                    #name below are only here as these need formatting
                    nm = name.text.replace('\n','')                                         #name of company
                    dt = Sdate.text.replace('\n','').replace('Immediately','').strip()      #date of joining as intern
                    #name above are only here as these need formatting

                    answer={
                        'Company name' : nm,
                        'Stipend' :  sal.text,
                        'Location': loc.text,
                        'Date of joining as intern' : dt,
                        'For more information link for internship': start_link+LK.a['href']
                        }

                    queries_json = json.dumps(answer)
                    all_answers.append(queries_json)

            return jsonify (all_answers)
        







        if __name__ == '__main__':
            app.run(debug=False, host='0.0.0.0', port=1000)


#case 4
    elif(case == 4):
        app = Flask(__name__)
        @app.route('/')
        def Data_Science_Development_internships():
            '''Function provide data for IOS development internship's from intershala.'''
            all_answers = []
            html_text = requests.get('https://internshala.com/internships/data%20science-internship?utm_source=homepage_modal_internship_search').text                  #for game development
            soup= BeautifulSoup (html_text,'lxml')


            company_name= soup.find_all('div', class_="heading_4_5 profile")
            stipend = soup.find_all(('span'), class_="stipend")
            location = soup.find_all(('a'), class_="location_link")
            start_date = soup.find_all(('div'), class_="item_body", id="start-date-first")
            link_to = soup.find_all(('div'),class_="heading_4_5 profile")



            for x in zip(company_name):
                for name, sal, loc, Sdate, LK in zip(company_name, stipend, location, start_date, link_to):                            #zip takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
   
                    #name below are only here as these need formatting
                    nm = name.text.replace('\n','')                                         #name of company
                    dt = Sdate.text.replace('\n','').replace('Immediately','').strip()      #date of joining as intern
                    #name above are only here as these need formatting

                    answer={
                        'Company name' : nm,
                        'Stipend' :  sal.text,
                        'Location': loc.text,
                        'Date of joining as intern' : dt,
                        'For more information link for internship': start_link+LK.a['href']
                        }

                    queries_json = json.dumps(answer)
                    all_answers.append(queries_json)

            return jsonify (all_answers)






        if __name__ == '__main__':
            app.run(debug=False, host='0.0.0.0', port=4000)


#case 5
    elif(case == 5):
        app = Flask(__name__)
        @app.route('/')
        def Data_Science_Development_internships():
            '''Function provide data for Data science internship's from intershala.'''
            all_answers = []
            html_text = requests.get('https://internshala.com/internships/data%20science-internship?utm_source=homepage_modal_internship_search').text                  #for game development
            soup= BeautifulSoup (html_text,'lxml')


            company_name= soup.find_all('div', class_="heading_4_5 profile")
            stipend = soup.find_all(('span'), class_="stipend")
            location = soup.find_all(('a'), class_="location_link")
            start_date = soup.find_all(('div'), class_="item_body", id="start-date-first")
            link_to = soup.find_all(('div'),class_="heading_4_5 profile")



            for x in zip(company_name):
                for name, sal, loc, Sdate, LK in zip(company_name, stipend, location, start_date, link_to):                            #zip takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
   
                    #name below are only here as these need formatting
                    nm = name.text.replace('\n','')                                         #name of company
                    dt = Sdate.text.replace('\n','').replace('Immediately','').strip()      #date of joining as intern
                    #name above are only here as these need formatting

                    answer={
                        'Company name' : nm,
                        'Stipend' :  sal.text,
                        'Location': loc.text,
                        'Date of joining as intern' : dt,
                        'For more information link for internship': start_link+LK.a['href']
                        }

                    queries_json = json.dumps(answer)
                    all_answers.append(queries_json)

            return jsonify (all_answers)






        if __name__ == '__main__':
            app.run(debug=False, host='0.0.0.0', port=4000)



#case 6
    elif(case == 6):
        app = Flask(__name__)
        @app.route('/')
        def Software_Development_internships():
            all_answers = []                                                   #list for getting the json files to post to local server as without it it dosent work
            html_text = requests.get('https://internshala.com/internships/software%20development-internship?utm_source=homepage_modal_internship_search').text                  #for game development
            soup= BeautifulSoup (html_text,'lxml')


            company_name= soup.find_all('div', class_="heading_4_5 profile")
            stipend = soup.find_all(('span'), class_="stipend")
            location = soup.find_all(('a'), class_="location_link")
            start_date = soup.find_all(('div'), class_="item_body", id="start-date-first")
            link_to = soup.find_all(('div'),class_="heading_4_5 profile")



            for x in zip(company_name):
                for name, sal, loc, Sdate, LK in zip(company_name, stipend, location, start_date, link_to):                            #zip takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
   
                    #name below are only here as these need formatting
                    nm = name.text.replace('\n','')                                         #name of company
                    dt = Sdate.text.replace('\n','').replace('Immediately','').strip()      #date of joining as intern
                    #name above are only here as these need formatting

                    answer={
                        'Company name' : nm,
                        'Stipend' :  sal.text,
                        'Location': loc.text,
                        'Date of joining as intern' : dt,
                        'For more information link for internship': start_link+LK.a['href']
                        }

                    queries_json = json.dumps(answer)
                    all_answers.append(queries_json)

            return jsonify (all_answers)




        if __name__ == '__main__':
            app.run(debug=False, host='0.0.0.0', port=3000)                         #Software_Development_internships


    else:
        print('\n\n\n\n**************************************   INVALID INPUT PLEASE RENTER YOUR CHOICE  **************************************')

        


    print("\n\n\n\n\nEnter '1' for getting important nortification from the JUIT website \nEnter '2' for getting internship data from the intershala\nEnter '3' for exiting the code")
    case = int(input('Enter your choice: - '))


print('''********************************** Exiting the JUIT scraper API on local host server **********************************
********************************** Thankyou for using our services **********************************''')