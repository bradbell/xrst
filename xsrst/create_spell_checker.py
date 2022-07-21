# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Create a pyspellchecker object
#
# local_words:
# a list of words that get addeed to the dictionary for this spell checker.
#
# spell_checker:
# The return spell_checker is a pyspellchecker spell checking object.
# 1. All single letter words are in its dictionary.
# 2. The latex command fo all the greek letters are in its dictionary.
#
import spellchecker
import string
def create_spell_checker(local_words) :
    assert type(local_words) == list
    if len(local_words) > 0 :
        assert type(local_words[0]) == str
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
    # spell_checker
    # add all the single letter words that are missing from the dictionary
    single_letter_word = list( string.ascii_lowercase )
    single_letter_word = spell_checker.unknown( single_letter_word )
    spell_checker.word_frequency.load_words(single_letter_word)
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
        'destructor',
        'exponentiation',
        'hessians',
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
        'pdf',
        'piecewise',
        'unary',
        'unicode',
        'wiki',
        'wikipedia',
        # END_SORT_THIS_LINE_MINUS_1
        #
        # greek letter latex commands
        # BEGIN_SORT_THIS_LINE_PLUS_1
        r'\Delta',
        r'\Gamma',
        r'\Lambda',
        r'\Omega',
        r'\Phi',
        r'\Pi',
        r'\Sigma',
        r'\Theta',
        r'\Upsilon',
        r'\Xi',
        r'\alpha',
        r'\beta',
        r'\chi',
        r'\delta',
        r'\epsilon',
        r'\eta',
        r'\gamma',
        r'\iota',
        r'\kappa',
        r'\lambda',
        r'\mu',
        r'\nu',
        r'\omega',
        r'\omicron',
        r'\phi',
        r'\pi',
        r'\psi',
        r'\rho',
        r'\sigma',
        r'\tau',
        r'\theta',
        r'\upsilon',
        r'\xi',
        r'\zeta',
        # END_SORT_THIS_LINE_MINUS_1
        #
        # common latex commands
        # BEGIN_SORT_THIS_LINE_PLUS_1
        r'\exp',
        r'\log',
        r'\rightarrow',
        # END_SORT_THIS_LINE_MINUS_1
    ]
    spell_checker.word_frequency.load_words(add_to_dictionary)
    # -------------------------------------------------------------------------
    # Add local spelling list to dictionary at end (never removed)
    spell_checker.word_frequency.load_words(local_words)
    #
    return spell_checker
