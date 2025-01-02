# DocCloud Tool

A simple TUI tool to enable interacting with DocumentCloud from the comfort of the terminal/IDE/whatever. Uses the [python-documentcloud](https://github.com/muckrock/python-documentcloud) wrapper of the DocumentCloud API.

### TODO (last updated Jan 1 2025) ###
- Implement upload functionality
- Implement document browsing/viewing/editing/delete functionality
  - Includes viewing the full text of the document as parsed by DocumentCloud

At some point I'd also like to convert this app into a proper CLI tool using something like the [Typer](https://github.com/fastapi/typer) library. But for the time being I'm happy with it being a simple program reading text from standard input. The main things preventing me from moving forward with Typer are a lack of understanding of how to manage persistent data (think DocumentCloud login info, or the Client object used to interact with the API) with a CLI tool.
