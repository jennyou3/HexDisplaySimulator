#ifndef MASKS
#define MASKS

#include <stdio.h>

typedef const uint8_t mask_array_t;
typedef const struct {
  const uint8_t height; 
  const uint8_t width; 
  const mask_array_t *mask_array;
} mask_t;


static mask_array_t mask_array_zero[] = {0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b01111110, 0b00100000, 0b00001000, 0b00000100, 0b00000010, 0b00000001, 0b10000001, 0b01000000, 0b00100000, 0b00001000, 0b11111100, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b0, };
static mask_t mask_zero = {22, 8, mask_array_zero};

static mask_array_t mask_array_one[] = {0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000010, 0b00100000, 0b00000000, 0b00000100, 0b00000000, 0b11111111, 0b00000001, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b0, };
static mask_t mask_one = {22, 8, mask_array_one};

static mask_array_t mask_array_heart[] = {0b00000000, 0b00000000, 0b00000000, 0b11000000, 0b00000001, 0b00010010, 0b00100000, 0b00000010, 0b10001000, 0b00000000, 0b01000100, 0b00000000, 0b00010001, 0b00100000, 0b00000010, 0b00100100, 0b11000000, 0b00000001, 0b00000000, 0b00000000, 0b00000000, 0b0, };
static mask_t mask_heart = {22, 8, mask_array_heart};

static mask_array_t mask_array_feesh[] = {0b00000000, 0b11111111, 0b11111000, 0b11000000, 0b00000011, 0b00011100, 0b11000000, 0b00000111, 0b11111010, 0b00000000, 0b01111111, 0b00000000, 0b00011111, 0b11000000, 0b00000011, 0b00111000, 0b10000000, 0b00000001, 0b00000000, 0b00000000, 0b00000000, 0b0, };
static mask_t mask_feesh = {22, 8, mask_array_feesh};


static const struct {
    mask_t *const mask;
    const char *name;
} mask_table[] = {
    {&mask_zero, "zero"},
    {&mask_one, "one"},
    {&mask_heart, "heart"},
    {&mask_feesh, "feesh"},
};

#endif
