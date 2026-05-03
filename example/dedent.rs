// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2020-26 Bradley M. Bell
// ----------------------------------------------------------------------------
/*
{xrst_begin literal_dedent_example}

Example Using dedent in Literal Command
#######################################

Example dedent Output
*********************
{xrst_literal , ///
    // BEGIN_EXAMPLE, // END_EXAMPLE
}

This Example File
*****************
{xrst_literal}

{xrst_end literal_dedent_example}
*/
mod module {
    /// ```
    // BEGIN_EXAMPLE
    /// use package::module::factorial;
    /// assert_eq!(factorial(3), 6 );
    // END_EXAMPLE
    /// ```
    pub fn factorial(n: u64) -> u64 {
        (1..=n).product()
    }
}
