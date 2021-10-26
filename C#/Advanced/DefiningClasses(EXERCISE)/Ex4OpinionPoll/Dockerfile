FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex4OpinionPoll/Ex4OpinionPoll.csproj", "Ex4OpinionPoll/"]
RUN dotnet restore "Ex4OpinionPoll/Ex4OpinionPoll.csproj"
COPY . .
WORKDIR "/src/Ex4OpinionPoll"
RUN dotnet build "Ex4OpinionPoll.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex4OpinionPoll.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex4OpinionPoll.dll"]
