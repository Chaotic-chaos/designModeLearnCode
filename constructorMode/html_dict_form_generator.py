# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 上午10:43
# @Author  : chaos
# @FileName: html_dict_form_generator.py
# @Software: PyCharm

def generate_text_field(field_dict):
    return '{0}:<br><input type="text" name="{1}"><br>'.format(field_dict["label"], field_dict["name"])


def generate_checkbox(field_dict):
    return '<label><input type="checkbox" id="{0}" value="{1}"> {2} <br>'.format(
        field_dict["id"],
        field_dict["value"],
        field_dict["label"]
    )


def generate_webform(field_dict_list):
    generated_list = []

    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            field_html = generate_text_field(field_dict)
        elif field_dict["type"] == "checkbox":
            field_html = generate_checkbox(field_dict)
        generated_list.append(field_html)
    generated_fields = "\n".join(generated_list)
    return "<form>{fields}</form>".format(fields = generated_fields)

def build_html_form(field_list):
    with open("form_file.html", "w") as file:
        file.write(
            "<html><body>{}</body></html>".format(
                generate_webform(field_list)
            )
        )


if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text"
        },

        {
            "type": "checkbox",
            "id": "check_it",
            "value": "1",
            "label": "check for one"
        },

        {
            "type": "text_field",
            "label": "Another text field",
            "name": "text_field_2"
        }
    ]

    build_html_form(field_list)