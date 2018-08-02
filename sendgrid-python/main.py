import sendgrid
import os

sg = sendgrid.SendGridAPIClient(apikey='____KEY____')
data = {
    "personalizations": [{
        "to": [{
            "email": "tanyapronto@litmustest.com"
        }],
        "dynamic_template_data": {
            "subject":
            "TESTING_01",
            "preheader":
            "How likely are you to recommend SimpleSat to a friends of colleague?",
            "answer_0_url":
            "https://simplesat.io",
            "answer_1_url":
            "https://simplesat.io",
            "answer_2_url":
            "https://simplesat.io",
            "answer_3_url":
            "https://simplesat.io",
            "answer_4_url":
            "https://simplesat.io",
            "answer_5_url":
            "https://simplesat.io",
            "answer_6_url":
            "https://simplesat.io",
            "answer_7_url":
            "https://simplesat.io",
            "answer_8_url":
            "https://simplesat.io",
            "answer_9_url":
            "https://simplesat.io",
            "answer_10_url":
            "https://simplesat.io",
            "company_url":
            "https://simplesat.io",
            "question":
            "How likely are you to recommend SimpleSat to a friends of colleague?",
            "logo_src":
            "https://marketing-image-production.s3.amazonaws.com/uploads/62ea04963ad40b9f7201d1b5b30692b59448cd9bc67fdf0dc06d784b1fe5df9ea1645c3f3604b7a6928cb1edc11b331cd951f30fb5b2a84e9d03ea29cc50a04e.png",
            "address":
            "Rajanakarn Building 3rd Floor, 15 Soi Pradipat 17 Pradipat Road, Samsennai, Phayathai, Bangkok 10400",
            "left_nps_footer":
            "Not likely at all",
            "right_nps_footer":
            "Very likely",
        },
    }],
    "from": {
        "email": "test@example.com"
    },
    "template_id":
    "d-333256acf88c42f28056cd9ee3bf8381",
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)