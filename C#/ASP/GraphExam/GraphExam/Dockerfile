FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["GraphExam/GraphExam.csproj", "GraphExam/"]
RUN dotnet restore "GraphExam/GraphExam.csproj"
COPY . .
WORKDIR "/src/GraphExam"
RUN dotnet build "GraphExam.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "GraphExam.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "GraphExam.dll"]
