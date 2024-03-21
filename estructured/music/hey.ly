\version "2.24.3"

\paper {
  print-page-number = false
  bottom-margin = 0\cm
  oddFooterMarkup = \markup {
    \column { }
  }
}

\score {
  \new Staff {
    \set Staff.midiInstrument = #"cello"
    \new Voice {
      \relative {
        c d e f g a b c
      }
    }
  }
  \layout {}
  \midi {}
}
