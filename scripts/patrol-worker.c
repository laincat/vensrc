#define _GNU_SOURCE
#include <fcntl.h>
#include <linux/landlock.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/prctl.h>
#include <sys/syscall.h>
#include <unistd.h>

#ifndef LANDLOCK_ACCESS_FS_TRUNCATE
#define LANDLOCK_ACCESS_FS_TRUNCATE (1ULL << 14)
#endif

int main(int argc, char **argv) {
    const char *directory = getenv("VENERA_RUNTIME_DATA_DIR");
    if (!directory || argc < 2) return 1;
    const struct landlock_ruleset_attr rules = {
        .handled_access_fs = LANDLOCK_ACCESS_FS_WRITE_FILE | LANDLOCK_ACCESS_FS_TRUNCATE |
            LANDLOCK_ACCESS_FS_REMOVE_DIR | LANDLOCK_ACCESS_FS_REMOVE_FILE |
            LANDLOCK_ACCESS_FS_MAKE_CHAR | LANDLOCK_ACCESS_FS_MAKE_DIR | LANDLOCK_ACCESS_FS_MAKE_REG |
            LANDLOCK_ACCESS_FS_MAKE_SOCK | LANDLOCK_ACCESS_FS_MAKE_FIFO | LANDLOCK_ACCESS_FS_MAKE_BLOCK |
            LANDLOCK_ACCESS_FS_MAKE_SYM | LANDLOCK_ACCESS_FS_REFER
    };
    int ruleset = syscall(SYS_landlock_create_ruleset, &rules, sizeof(rules), 0);
    int scratch = open(directory, O_PATH | O_DIRECTORY | O_NOFOLLOW | O_CLOEXEC);
    const struct landlock_path_beneath_attr writable = {
        .allowed_access = rules.handled_access_fs, .parent_fd = scratch
    };
    if (ruleset < 0 || scratch < 0 ||
        syscall(SYS_landlock_add_rule, ruleset, LANDLOCK_RULE_PATH_BENEATH, &writable, 0) ||
        prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) || syscall(SYS_landlock_restrict_self, ruleset, 0)) {
        perror("patrol worker filesystem isolation");
        return 1;
    }
    close(scratch);
    close(ruleset);
    if (setenv("TMPDIR", directory, 1)) return 1;
    execv("/usr/local/bin/node", argv);
    perror("node");
    return 1;
}
