FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1DefineClassPerson/Ex1DefineClassPerson.csproj", "Ex1DefineClassPerson/"]
RUN dotnet restore "Ex1DefineClassPerson/Ex1DefineClassPerson.csproj"
COPY . .
WORKDIR "/src/Ex1DefineClassPerson"
RUN dotnet build "Ex1DefineClassPerson.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1DefineClassPerson.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1DefineClassPerson.dll"]
