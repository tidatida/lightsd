FUNCTION(ADD_TEST_FROM_C_SOURCES TEST_SOURCE TEST_LIB)
    STRING(LENGTH ${TEST_SOURCE} TEST_NAME_LEN)
    STRING(LENGTH "test_" PREFIX_LEN)
    MATH(EXPR TEST_NAME_LEN "${TEST_NAME_LEN} - 2 - ${PREFIX_LEN}")
    STRING(SUBSTRING ${ARGV0} ${PREFIX_LEN} ${TEST_NAME_LEN} TEST_NAME)
    ADD_EXECUTABLE(${TEST_NAME} ${TEST_SOURCE} ${ARGN})
    IF (TEST_LIB)
        TARGET_LINK_LIBRARIES(${TEST_NAME} ${TEST_LIB})
    ENDIF ()
    ADD_TEST(test_${TEST_NAME} ${TEST_NAME})
ENDFUNCTION()
