import mariadb

# spell_list.jobs and weapon_skills.jobs store one byte per job, WAR (1) first.
# The old binary(22) held WAR..RUN. binary(24) holds jobs 1-24 (WAR..ORA), so the
# MON byte (23) and ORA byte (24) are new. ALTER pads existing values with 0x00,
# which means "no level" for those two jobs.
TABLES = ["spell_list", "weapon_skills"]


def migration_name():
    return "Widening jobs column to binary(24) in spell_list and weapon_skills"


def check_preconditions(cur):
    return


def needs_to_run(cur):
    for table in TABLES:
        cur.execute("SHOW COLUMNS FROM {} LIKE 'jobs'".format(table))
        row = cur.fetchone()
        if row and "binary(24)" not in str(row[1]).lower():
            return True
    return False


def migrate(cur, db):
    try:
        for table in TABLES:
            cur.execute("SHOW COLUMNS FROM {} LIKE 'jobs'".format(table))
            row = cur.fetchone()
            if row and "binary(24)" not in str(row[1]).lower():
                cur.execute(
                    "ALTER TABLE {} MODIFY COLUMN `jobs` binary(24) NOT NULL;".format(
                        table
                    )
                )
        db.commit()
    except mariadb.Error as err:
        print("Something went wrong: {}".format(err))
