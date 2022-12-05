# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import spellchecker
# {xrst_begin create_spell_checker dev}
# {xrst_spell
#     len
#     pyspellchecker
# }
# {xrst_comment_ch #}
#
# Create a pyspellchecker object
# ##############################
#
# Arguments
# *********
#
# local_words
# ===========
# a list of words that get added to the dictionary for this spell checker.
# No need to add single letter words because they are considered correct
# by spell_command routine.
#
# Returns
# *******
#
# spell_checker
# =============
# The return spell_checker is a pyspellchecker spell checking object.
#
# {xrst_code py}
def create_spell_checker(local_words) :
   assert type(local_words) == list
   if len(local_words) > 0 :
      assert type(local_words[0]) == str
   # {xrst_code}
   # {xrst_literal
   #  BEGIN_return
   #  END_return
   # }
   # {xrst_end create_spell_checker}
   #
   # spell_checker
   spell_checker = spellchecker.SpellChecker(distance=1)
   #
   # remove_from_dictionary
   # list of words that, if they are in the dictionary, are removed
   remove_from_dictionary = [
      # BEGIN_SORT_THIS_LINE_PLUS_1
      'af',
      'anl',
      'ap',
      'av',
      'bnd',
      'bv',
      'cg',
      'conf',
      'cpp',
      'dep',
      'dir',
      'dv',
      'exp',
      'gcc',
      'hes',
      'hess',
      'ind',
      'jac',
      'len',
      'mcs',
      'meas',
      'nc',
      'nd',
      'nr',
      'op',
      'prt',
      'ptr',
      'rc',
      'rel',
      'sim',
      'std',
      'tbl',
      'thier',
      'var',
      'vec',
      'xp',
      'yi',
      # END_SORT_THIS_LINE_MINUS_1
   ]
   #
   # spell_checker
   remove_from_dictionary = spell_checker.known( remove_from_dictionary )
   spell_checker.word_frequency.remove_words(remove_from_dictionary)
   #
   # add_to_dictionary
   # list of
   add_to_dictionary = [
      # BEGIN_SORT_THIS_LINE_PLUS_1
      'aborts',
      'asymptotic',
      'configurable',
      'covariate',
      'covariates',
      'debug',
      'deprecated',
      'destructor',
      'exponentiation',
      'hessians',
      'html',
      'identifiability',
      'indenting',
      'initialization',
      'initialize',
      'initialized',
      'integrand',
      'integrands',
      'invertible',
      'jacobian',
      'jacobians',
      'likelihoods',
      'messaging',
      'modeled',
      'modeling',
      'multipliers',
      'optimizes',
      'partials',
      'tex',
      'piecewise',
      'subdirectory',
      'unary',
      'unicode',
      'verbose',
      'wiki',
      'wikipedia',
      'xrst',
      # END_SORT_THIS_LINE_MINUS_1
   ]
   spell_checker.word_frequency.load_words(add_to_dictionary)
   # -------------------------------------------------------------------------
   # Add local spelling list to dictionary at end (never removed)
   spell_checker.word_frequency.load_words(local_words)
   #
   # BEGIN_return
   return spell_checker
   # END_return
