name "stage"
description "Sophi Staging Environment"

default_attributes \
    "aws" => {
        "database_host" => "stage.AAAAAAAAAAAA.us-west-2.rds.amazonaws.com",
        "storage_bucket" => "stage-c2g",
        "access_key" => "BBBBBBBBBBBBBBBBBBBB",
        "access_secret" => "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
        "ses_user" =>  "DDDDDDDDDDDDDDDDDDDD",
        "ses_passwd" => "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
    },
    "sophi" => {
        "production" => "False",
        "admin_name" => "Sophi Operations",
        "admin_email" => "sophi-ops@cs.stanford.edu"
    },
    "piazza" => {
        "endpoint" => "https://piazza.com/basic_lti",
        "key" => "sophi",
        "secret" => "XXXXXXXXXXXXXXXXXXXXXXXXX"
    }

