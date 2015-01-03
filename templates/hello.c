$header_banner

/** 
 * \file $project_name
 */

#include <stdio.h>
#include "$project_name.h"

/**
 * print_output() for project $project_name  
 * 
 * parameter: str - a string that will be published to stdout 
 *           
 * returns: 0 on success
 */
int print_output(char* str){
  printf("%s\n", str);
  return(0);
}

#ifndef TEST_OPERATIONS
/**
 * main() for project $project_name with unit tests
 */
int main(int argc, char** argv) {
     unit_tests();
     return(0);
}
#else
/**
 * main() for project $project_name
 */
int main(int argc, char** argv) {
  char str[20] = "Hello World";
     print_output(str);
     return(0);
}
#endif
