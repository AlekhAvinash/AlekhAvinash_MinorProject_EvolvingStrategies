# EvolvingStrategies

The application is based on a recent study that found LLMs can behave as rational players in a game theoretic environment. This study furthers the results by testing rational player behaviors in evolving games.

The application is structured in three layers. The highest layer is the tournament class. Which can be used to run a tournament, and decide the following:
- Which two players (LLMs or Static Strategy) will be used during the tournament.
- The weight/rewards for the game (optional delta value to dial the change of rewards during the game).
- Number of rounds.

The next level is the game class which facilitates, the actual game in a particular round. It also keeps track of the past rounds and their results and the player objects.

The lowest level is the player class who simply calls the Strategy/LLMs for a response and sends back the results.

# Application Structure

![Design](https://github.com/user-attachments/assets/93a4d248-5adf-4992-a2fc-803a3880ebcb)
