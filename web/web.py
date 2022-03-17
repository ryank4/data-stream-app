from flask import Flask
import redis

app = Flask(__name__)
conn = redis.StrictRedis(host='redis', port=6379, charset="utf-8", decode_responses=True)


@app.route('/')
def show_metrics():
    try:
        output = "<table>"

        output += "<thead><tr><th>Total Arrests Made</th></tr></thead>"
        num_arrests = conn.get("ArrestsMade")
        output += "<thead><tr><th>" + num_arrests + "</th>" + "</th</tr>"

        output += "<thead><tr><th>Age Group with Most Violations</th></tr></thead>"
        age_group = conn.get("AgeGroupMostViolations")
        output += "<thead><tr><th>" + age_group + "</th>" + "</th</tr>"

        output += "<thead><tr><th>Violations in the last minute</th></tr></thead>"
        violations_last_minute = conn.get("ViolationsLastMinute")
        output += "<thead><tr><th>" + violations_last_minute + "</th>" + "</th</tr>"

        output += "<thead><tr><th>Drugs Related Violations</th></tr></thead>"
        drugs = conn.get("DrugsRelated")
        output += "<thead><tr><th>" + drugs + "</th>" + "</th</tr>"

        output += "<tbody>"
        output += '''</tbody>
                        </table'''
    except Exception as ex:
        output = 'Error:' + str(ex)

    return output


def show_rolling_metric():
    try:
        output = '''<table>
        <thead><tr><th>Violation</th><th>Count</th></tr></thead>
        <tbody>'''
        for key in conn.scan_iter("Violation:*"):
            value = str(conn.get(key))
            violation = str(key).split(":")
            output += "<tr><td>" + violation[1] + "</td><td>" + value + "</td></tr>"

        output += '''</tbody>
                     </table'''
    except Exception as ex:
        output = 'Error:' + str(ex)

    return output


def show_age_metric():
    try:
        output = '''<table>
                    <thead><tr><th>Age Group with Most Violations</th></tr></thead>'''
        output += "<thead><tr><th>Age Group</th><th>Count</th></tr></thead>"
        age_group = conn.get("AgeGroupMostViolations")
        age_group_violation_count = conn.get("AgeGroupMostViolationsCount")
        output += "<thead><tr><th>" + age_group + "</th>" + "<th>" + age_group_violation_count + "</th</tr></thead>"
        output += "<tbody>"
        output += '''</tbody>
                     </table'''
    except Exception as ex:
        output = 'Error:' + str(ex)

    return output


def show_other_metrics():
    try:
        output = "<table>"

        arrests_made = "Total Arrests Made"
        total_arrests_made = conn.get("ArrestsMade")
        output += "<thead><tr><th>" + arrests_made + "</th></tr></thead>"
        output += "<tr><td>" + total_arrests_made + "</td></tr>"

        drugs_found = "Times drugs were found after search was conducted"
        times_drugs_found = conn.get("SearchDrugsFound")
        output += "<thead><tr><th>" + drugs_found + "</th></tr></thead>"
        output += "<tr><td>" + times_drugs_found + "</td></tr>"

        output += '''</tbody>
                         </table'''
    except Exception as ex:
        output = 'Error:' + str(ex)

    return output

def show_metrics():
    try:
        output = "<table>"

        output += "<thead><tr><th>Total Arrests Made</th></tr></thead>"
        num_arrests = conn.get("ArrestsMade")
        output += "<thead><tr><th>" + num_arrests + "</th>" + "</th</tr>"

        output += "<thead><tr><th>Age Group with Most Violations</th></tr></thead>"
        age_group = conn.get("AgeGroupMostViolations")
        output += "<thead><tr><th>" + age_group + "</th>" + "</th</tr>"

        output += "<thead><tr><th>Violations in the last minute</th></tr></thead>"
        violations_last_minute = conn.get("ViolationsLastMinute")
        output += "<thead><tr><th>" + violations_last_minute + "</th>" + "</th</tr>"

        output += "<thead><tr><th>Drugs Related Violations</th></tr></thead>"
        drugs = conn.get("DrugsRelated")
        output += "<thead><tr><th>" + drugs + "</th>" + "</th</tr>"

        output += "<tbody>"
        output += '''</tbody>
                     </table'''
    except Exception as ex:
        output = 'Error:' + str(ex)

    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

