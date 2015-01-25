#include <stdio.h>
#include "minunit.h"
#include "$project_name.h"

int tests_run = 0;

static char* test_01_$project_name(void) {
  mu_assert("error: print_output() != Hello World", print_output("Hello World") == 0);
  /* return(0); */
}

static char*  test_02_$project_name(void) {
  mu_assert("error: print_output() != Goodbye World", print_output("Goodbye World") == 0);
  /* return(0); */
}

static char*  all_tests(void) {
  mu_run_test(test_01_$project_name);
  mu_run_test(test_02_$project_name);
  return(0);

}
int unit_tests ( void )
{
  char* result = all_tests();
  if (result != 0) {
    printf("%s\n", result);
  } else {
    printf("All tests passed \n");
  }
  printf("Tests run: %d\n", tests_run);
  return result != 0;
}
