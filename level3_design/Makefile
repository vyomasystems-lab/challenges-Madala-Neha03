# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/shift_register.v               # provide your design path

TOPLEVEL :=   shift_register       # design file
MODULE   :=   test_shift_register  # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
