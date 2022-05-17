#' R6 class for keyword analysis
#'
#' TBD
#' @export
KeywordFinder <- R6::R6Class("KeywordFinder", list(
  initialize = function(
    positive_keywords = NA,
    negative_keywords = NA) {

    self$positive_keywords = positive_keywords
    self$negative_keywords = negative_keywords

    # TODO: more processing from python code.

  },

  find_keywords = function() {
  },

  score_sentiment = function() {
  },

  run = function(text) {
  },

  print = function(...) {
    cat("Positive keywords:", len(self$positive_keywords), "\n")
    cat("Negative keywords:", len(self$negative_keywords), "\n")
    invisible(self)
  }
))
