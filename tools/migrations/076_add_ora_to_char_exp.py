import mariadb


def migration_name():
    return "Adding ORA (job 24) to char_exp table"


def check_preconditions(cur):
    return


def needs_to_run(cur):
    cur.execute("SHOW COLUMNS FROM char_exp LIKE 'ora'")
    if not cur.fetchone():
        return True
    return False


def migrate(cur, db):
    try:
        cur.execute(
            "ALTER TABLE char_exp \
                ADD COLUMN `ora` smallint(5) unsigned NOT NULL DEFAULT '0';"
        )
        db.commit()
    except mariadb.Error as err:
        print("Something went wrong: {}".format(err))
