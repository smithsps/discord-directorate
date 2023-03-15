defmodule DiscordBot.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # Start the Ecto repository
      DiscordBot.Repo,
      # Start the PubSub system
      {Phoenix.PubSub, name: DiscordBot.PubSub},
      # Start Finch
      {Finch, name: DiscordBot.Finch}
      # Start a worker by calling: DiscordBot.Worker.start_link(arg)
      # {DiscordBot.Worker, arg}
    ]

    Supervisor.start_link(children, strategy: :one_for_one, name: DiscordBot.Supervisor)
  end
end
