QT_VERSION?=PyQt4
export QT_VERSION


ifeq ($(QT_VERSION),PyQt5)
  PYUIC = pyuic5
  PYRCC = pyrcc5
  PYLUPDATE = pylupdate5
else ifeq ($(QT_VERSION),PyQt4)
  PYUIC = pyuic4
  PYRCC = pyrcc4
  PYLUPDATE = pylupdate4
else ifeq ($(QT_VERSION),PySide)
  PYUIC = pyside-uic
  PYRCC = pyside-rcc
  PYLUPDATE = pylupdate4
else
  PYUIC = pyuic4
  PYRCC = pyrcc4
  PYLUPDATE = pylupdate4
endif

UI_FILES = $(shell ls *.ui)
UI_COMPILED = $(patsubst %.ui, ui_%.py, $(UI_FILES))
RC_FILES = $(shell ls *.qrc)
RC_COMPILED = $(patsubst %.qrc, %_rc.py, $(RC_FILES))

all: $(UI_COMPILED) $(RC_COMPILED)

clean:
	rm -f $(UI_COMPILED) $(RC_COMPILED)
	rm -rf *.pyc *~ __pycache__

ui_%.py:  %.ui
	$(PYUIC) --from-import $< -o $@

%_rc.py: %.qrc
	$(PYRCC) $< -o $@

.PHONY: all clean
