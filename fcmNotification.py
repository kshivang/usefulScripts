# To run this script use python fcmNotification.py or python *.py, where * is you file name
# This is python script to send fcm notification with payload or data
# I haved used documentation from  "https://github.com/olucurious/PyFCM"

from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyC41OgOOzW27O8Dt_ZvIqbA5Tt3PaVhyLw")

# Comment out below code for proxy server

# proxy_dict = {
        # "http" : "http://127.0.0.1",
        # "https" : "http://127.0.0.1",
        # }
# push_service -FCMNotification(api_key"", proxy_dict=proxy_dict)


# registration_ids = "," for multiple device notification
registration_id = "duev9DEuV-o:APA91bHJreL63jKVc99Jennbwl3tULi8u2DmCCJECUYc45p6sExMUqd_jJT02ObZSzCFBCyzSGeDrFIrEfd_mjpr0qykCeGe8F7lx9uMf-nQ3SXVbAQ9WJ-dXMa8YTma5tPbMGhd_kUL"

# message title and body is for notification title and body
message_title = "Adurcup"
message_body = "This is body of message"

# data_message is data payload load in our case JSON object
data_message = {
                  "current_service" : {
                    "address_line_one" : "Shivanta Road jaisa kuch address, Malviya Nagar",
                    "address_line_two" : "MALVIYA NAGAR, DELHI",
                    "area" : 1200,
                    "date" : "20 July 2016",
                    "location" : "T'Pot Cafe",
                    "time" : "11:30 AM"
                  },

                  "outstanding_services" : [
                        {
                                "address_line_one" : "Some location, some other sub location, Location",
                                "address_line_two" : "MAIN AREA OF SERVICE",
                                "area" : 1000,
                                "date" : "20 July 2016",
                                "location" : "Some Restaurant",
                                "time" : "12:30 PM"
                        },
                        {
                                "address_line_one" : "Some location, some other sub location, Location",
                                "address_line_two" : "MAIN AREA OF SERVICE",
                                "area" : 1000,
                                "date" : "20 July 2016",
                                "location" : "Some Restaurant",
                                "time" : "12:30 PM"
                        },
                        {
                                "address_line_one" : "Some location, some other sub location, Location",
                                "address_line_two" : "MAIN AREA OF SERVICE",
                                "area" : 1000,
                                "date" : "20 July 2016",
                                "location" : "Some Restaurant",
                                "time" : "12:30 PM"
                        }
                  ]
        }

# push_service.notify_single_device is actuall fuction which send notification
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body, data_message=data_message)

# print notification reached data
print result
