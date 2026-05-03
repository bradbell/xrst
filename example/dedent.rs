// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2020-26 Bradley M. Bell
// ----------------------------------------------------------------------------
/*
{xrst_begin literal_dedent_example}

Example Using dedent in Literal Command
#######################################

Example Without dedent
**********************
In this literal example the output lines are exactly as they appear
in the display file:
{xrst_literal ,
    // BEGIN_SQUARE, // END_SQUARE
}

Example Where dedent Does Not Match
***********************************
In this literal example the leading spaces are removed:
{xrst_literal , %
    // BEGIN_TRIANGULAR, // END_TRIANGULAR
}

Example Where dedent Matches
****************************
In this literal example the leading spaces, the dedent characters,
and one space after the dedent characters are removed:
{xrst_literal , ///
    // BEGIN_FACTORIAL, // END_FACTORIAL
}

This Example File
*****************
{xrst_literal}

{xrst_end literal_dedent_example}
*/
pub mod module {
    /// ```
    // BEGIN_SQUARE
    /// use package::module::square;
    /// assert_eq!(square(5), 25 );
    // END_SQUARE
    /// ```
    pub fn square(n: u64) -> u64 {
        n * n
    }
    /// ```
    // BEGIN_TRIANGULAR
    /// use package::module::triangular;
    /// assert_eq!(triangular(4), 10 );
    // END_TRIANGULAR
    /// ```
    pub fn triangular(n: u64) -> u64 {
        (1..=n).sum()
    }
    /// ```
    // BEGIN_FACTORIAL
    /// use package::module::factorial;
    /// assert_eq!(factorial(4), 24 );
    // END_FACTORIAL
    /// ```
    pub fn factorial(n: u64) -> u64 {
        (1..=n).product()
    }
}
